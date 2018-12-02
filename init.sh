#!/usr/bin/env bash
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo kill -9 `sudo ps ax | grep 'gunicorn' | awk '{print $1}'`
sudo gunicorn hello:application -b 0.0.0.0:8080  &