#!/usr/bin/env bash
# don't forget that in gunicorn configs python 3.5 should be used
# all changed filed i added to an "edinorogs" directory
apt-get update
apt-get install -f python3.5
apt-get install python-mysqldb
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python3.5 get-pip.py
pip install django
pip install gunicorn
pip install pymysql

cp edinorogs/gunicorn-debian /usr/sbin/
cp edinorogs/gunicorn /usr/bin/
cp edinorogs/gunicorn_* /usr/bin/

mysql -uroot -e "create database ask CHARACTER SET utf8;"
mysql -uroot -e  "create user 'django'@'localhost' identified by 'django-user-password';"
mysql -uroot -e  "grant usage on *.* to 'django'@'localhost';"
mysql -uroot -e  "grant all privileges on ask.* to 'django'@'localhost';"
cd ask && ./manage.py migrate && cd ..