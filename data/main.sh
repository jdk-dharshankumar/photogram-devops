#! /bin/bash

touch /var/photogram/helloworld

git clone git@github.com:jdk-dharshankumar/photogram.git /var/www/html
mv /var/photogram/photogramconfig.json /var/www
# sed -i "s/short_open_tag = .*/short_open_tag = On/" /etc/php/7.4/apache2/php.ini
/usr/sbin/apache2ctl -D FOREGROUND
service apache2 start