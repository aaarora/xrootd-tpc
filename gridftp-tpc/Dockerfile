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

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
