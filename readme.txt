mkdir notes
cd notes
virtualenv env
. ./env/bin/activate
pip install -r requirements.txt
cd notes && pelican-themes -vi ../pelican-bootstrap3/
