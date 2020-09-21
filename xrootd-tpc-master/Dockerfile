FROM opensciencegrid/software-base:fresh

RUN yum -y install vim

RUN easy_install pip && \
    pip install requests 

RUN adduser master

RUN mkdir -p /var/log/supervisor
ADD supervisord.conf /etc/supervisord.conf
