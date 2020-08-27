FROM opensciencegrid/software-base:fresh

RUN yum -y install vim && \
    yum -y install osg-ca-certs && \
    yum -y install osg-gridftp && \
    yum -y install gfal2-util gfal2-plugin-http
    
RUN adduser tpcuser

RUN mkdir -p /var/run/sshd /var/log/supervisor
ADD supervisord.conf /etc/supervisord.conf
ADD gridftp.conf /etc/gridftp.conf
EXPOSE 2811 8888
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
