FROM opensciencegrid/software-base:fresh

RUN yum -y install vim && \
    yum -y install osg-ca-certs && \
    yum -y install osg-test osg-ca-generator --enablerepo=devops-itb && \
    yum -y install osg-gridftp && \
    yum -y install gfal2-plugin-file gfal2-plugin-gridftp && \
    yum -y install globus-gass-copy-progs
    
RUN adduser tpcuser

ADD image-config.d/* /etc/osg/image-config.d/

RUN mkdir -p /var/log/supervisor
ADD supervisord.conf /etc/supervisord.d/10-gridftp.conf

ADD grid-mapfile /etc/grid-security/grid-mapfile
