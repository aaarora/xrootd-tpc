FROM opensciencegrid/software-base:fresh

RUN yum -y install vim && \
    yum -y install osg-ca-certs && \
    yum -y install osg-gridftp && \
    yum -y install gfal2-plugin-file gfal2-plugin-gridftp && \
    yum -y install globus-gass-copy-progs
    
RUN adduser tpcuser

RUN mkdir -p /var/log/supervisor
ADD supervisord.conf /etc/supervisord.conf

ADD grid-mapfile /etc/grid-security/grid-mapfile
ADD gridftp.conf /etc/gridftp.conf
ADD globus-gridftp-server /etc/sysconfig/globus-gridftp-server

RUN mkdir /home/.globus/

EXPOSE 2811 50000-51000

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
