# don't forget that in gunicorn configs python 3.5 should be used
# all changed filed i added to an "edinorogs" directory
apt-get update
apt-get install -f python3.5
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python3.5 get-pip.py
pip install django
pip install gunicorn

cp edinorogs/gunicorn-debian /usr/sbin/
cp edinorogs/gunicorn /usr/bin/
cp edinorogs/gunicorn_* /usr/bin/