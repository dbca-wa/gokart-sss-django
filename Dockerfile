# Prepare the base environment.
FROM ubuntu:22.04 as builder_base_govapp
MAINTAINER asi@dbca.wa.gov.au

ENV DEBIAN_FRONTEND=noninteractive
#ENV DEBUG=True
ENV TZ=Australia/Perth
ENV DEFAULT_FROM_EMAIL='no-reply@dbca.wa.gov.au'
ENV NOTIFICATION_EMAIL='no-reply@dbca.wa.gov.au'
ENV NON_PROD_EMAIL='none@none.com'
ENV PRODUCTION_EMAIL=False
ENV EMAIL_INSTANCE='DEV'
ENV SECRET_KEY="ThisisNotRealKey"
ENV SITE_DOMAIN='dbca.wa.gov.au'


RUN apt-get clean
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install --no-install-recommends -y curl wget git libmagic-dev gcc binutils libproj-dev python3 python3-setuptools python3-dev python3-pip tzdata cron rsyslog gunicorn
RUN apt-get install --no-install-recommends -y libpq-dev patch libreoffice
RUN apt-get install --no-install-recommends -y postgresql-client mtr htop vim  sudo
RUN apt-get install --no-install-recommends -y bzip2 pdftk
RUN apt-get install --no-install-recommends -y build-essential
RUN apt-get install --no-install-recommends -y software-properties-common 
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install GDAL
RUN add-apt-repository ppa:ubuntugis/ubuntugis-unstable
RUN apt update
RUN apt-get install --no-install-recommends -y gdal-bin python3-gdal
RUN apt-get install --no-install-recommends -y libgdal-dev build-essential

# Install nodejs
RUN update-ca-certificates

WORKDIR /app

# install node 16
RUN touch install_node.sh
RUN curl -fsSL https://deb.nodesource.com/setup_18.x -o install_node.sh
RUN chmod +x install_node.sh && ./install_node.sh
RUN apt-get update
RUN apt-get install -y nodejs
RUN apt-get install -y uglifyjs
RUN pip install npm
RUN npm install -g browserify
RUN npm install -g npm-run-all
RUN npm install -g closure-util

# Install nodejs
COPY cron /etc/cron.d/dockercron
COPY startup.sh pre_startup.sh /
COPY ./timezone /etc/timezone
COPY sss sss
COPY packages packages
RUN chmod 0644 /etc/cron.d/dockercron && \
    crontab /etc/cron.d/dockercron && \
    touch /var/log/cron.log && \
    service cron start && \
    chmod 755 /startup.sh && \
    chmod +s /startup.sh && \
    chmod 755 /pre_startup.sh && \
    chmod +s /pre_startup.sh && \
    groupadd -g 5000 oim && \
    useradd -g 5000 -u 5000 oim -s /bin/bash -d /app && \
    usermod -a -G sudo oim && \
    echo "oim  ALL=(ALL)  NOPASSWD: /startup.sh" > /etc/sudoers.d/oim && \
    chown -R oim.oim /app && \
    mkdir /container-config/ && \
    chown -R oim.oim /container-config/ && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    touch /app/rand_hash

RUN chmod 755 /pre_startup.sh
# Install Python libs from requirements.txt.
FROM builder_base_govapp as python_libs_govapp

USER oim
RUN PATH=/app/.local/bin:$PATH
COPY --chown=oim:oim requirements.txt ./

RUN pip install -r requirements.txt
#\ && rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*

# Install the project (ensure that frontend projects have been built prior to this step).
FROM python_libs_govapp
COPY  --chown=oim:oim gunicorn.ini manage.py ./
RUN touch /app/.env

RUN python manage.py collectstatic --noinput

RUN mkdir /app/tmp/
RUN chmod 777 /app/tmp/

# IPYTHONDIR - Will allow shell_plus (in Docker) to remember history between sessions
# 1. will create dir, if it does not already exist
# 2. will create profile, if it does not already exist
#RUN mkdir /app/logs/.ipython
#RUN export IPYTHONDIR=/app/logs/.ipython/

EXPOSE 8080
HEALTHCHECK --interval=1m --timeout=5s --start-period=10s --retries=3 CMD ["wget", "-q", "-O", "-", "http://localhost:8080/"]
CMD ["/pre_startup.sh"]

