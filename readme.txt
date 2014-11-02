git clone ../znotdead.github.io
mkdir notes
cd notes
git clone https://..../notes.git
virtualenv env
. ./env/bin/activate
pip install -r requirements.txt

cd notes && pelican-themes -vi ../pelican-bootstrap3/

fab deploy_github
