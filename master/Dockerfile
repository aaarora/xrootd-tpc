FROM opensciencegrid/software-base:fresh

RUN yum -y install vim
RUN adduser master

RUN mkdir -p /var/log/supervisor
ADD supervisord.conf /etc/supervisord.conf

EXPOSE 8080
