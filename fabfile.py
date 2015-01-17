from fabric.api import *
import fabric.contrib.project as project
import os
import sys
import SimpleHTTPServer
import SocketServer

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

DROPBOX_FOLDER = os.path.join(os.getenv('HOME'), 'Dropbox/content/')
GIT_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'content/')
RSYNC_COMMAND = 'rsync -abuP --exclude *.swp --exclude *~'
GITHUB_LOCAL_REPO = '../../znotdead.github.io/'
LOCK_FILE = 'need_manual_commit.lock'

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    os.chdir(env.deploy_path)

    PORT = 8000
    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

def cf_upload():
    rebuild()
    local('cd {deploy_path} && '
          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          '-U {cloudfiles_username} '
          '-K {cloudfiles_api_key} '
          'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )

def deploy_github():
    # quit if lock exists
    with settings(warn_only=True):
        if not local('test -f %s' % LOCK_FILE).failed:
            print 'Need manual commit. Do not forget to remove lock.'
            return

    local('pelican content -o %s -s publishconf.py' % GITHUB_LOCAL_REPO)
    local('cd %s && git add * && git commit -m "deploy" && git push' % GITHUB_LOCAL_REPO)

def rsync_with_dropbox():
    local('%s %s %s' % (RSYNC_COMMAND, DROPBOX_FOLDER, GIT_FOLDER))
    local('%s %s %s' % (RSYNC_COMMAND, GIT_FOLDER, DROPBOX_FOLDER))
    local('touch %s' % LOCK_FILE)
