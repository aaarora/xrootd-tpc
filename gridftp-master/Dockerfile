FROM opensciencegrid/software-base:fresh

RUN yum -y install vim && \
    yum -y install gfal2-plugin-file gfal2-plugin-gridftp && \
    yum -y install globus-gass-copy-progs

RUN easy_install pip && \
    pip install requests 

RUN adduser master

RUN mkdir -p /var/log/supervisor
ADD supervisord.conf /etc/supervisord.conf
