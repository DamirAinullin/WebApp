#!/usr/bin/env bash
ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
rm -rf /etc/nginx/sites-enabled/default
/etc/init.d/nginx restart
#/etc/init.d/mysql restart

kill -9 `sudo ps ax | grep 'gunicorn' | awk '{print $1}'`
gunicorn -b 0.0.0.0:8080 hello:application &
cd ask && gunicorn -b 0.0.0.0:8000 ask.wsgi:application && cd .. &

