#!/usr/bin/env bash
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo kill -9 `sudo ps ax | grep 'gunicorn' | awk '{print $1}'`
sudo gunicorn -b 0.0.0.0:8080 hello:application &
cd ask && sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application && cd .. &



# don't forget that in gunicorn configs python 3.5 should be used
# all changed filed i added to an "edinorogs" directory
apt-get update
apt-get install -f python3.5
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python3.5 get-pip.py
pip install django
pip install gunicorn
rm /etc/nginx/sites-enabled/default
cp /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
cp /home/box/web/etc/gunicorn*.conf   /etc/gunicorn.d/
cp edinorogs/gunicorn-debian /usr/sbin/
cp edinorogs/gunicorn /usr/bin/
cp edinorogs/gunicorn_* /usr/bin/
/etc/init.d/nginx restart
/etc/init.d/gunicorn restart