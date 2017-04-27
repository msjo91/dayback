FROM        ubuntu:16.04
MAINTAINER  msjo91@gmail.com

COPY        . /srv/app

RUN         apt-get -y update
RUN         apt-get -y install python3
RUN         apt-get -y install python3-pip
RUN         apt-get -y install nginx
RUN         apt-get -y install supervisor

WORKDIR     /srv/app

RUN         pip3 install --upgrade pip
RUN         pip3 install --upgrade setuptools
RUN         pip3 install django
RUN         pip3 install -r requirements.txt
RUN         pip3 install uwsgi
COPY        .conf/uwsgi-app.ini          /etc/uwsgi/sites/app.ini
COPY        .conf/nginx.conf             /etc/nginx/nginx.conf
COPY        .conf/nginx-app.conf         /etc/nginx/sites-available/app.conf
COPY        .conf/supervisor-app.conf    /etc/supervisor/conf.d/

RUN         ln -s /etc/nginx/sites-available/app.conf   /etc/nginx/sites-enabled/app.conf

WORKDIR     /srv/app/django_app
EXPOSE      80
CMD         supervisord -n