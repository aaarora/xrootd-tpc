FROM opensciencegrid/software-base:fresh

RUN yum -y install maddash

ADD maddash.yaml /etc/maddash/maddash-server/
ADD esmondAPI /home/esmondAPI
ADD psconfig.json /home
ADD 10-maddash-server.conf /etc/supervisord.d/10-maddash-server.conf
ADD 10-httpd.conf /etc/supervisord.d/10-httpd.conf

CMD ["/bin/bash"]
