FROM opensciencegrid/software-base:fresh

RUN yum -y install vim && \
    yum -y install osg-ca-certs && \
    yum -y install osg-xrootd-standalone --enablerepo=osg-upcoming-development
    

ADD fetch-crl-kubernetes /etc/cron.d/fetch-crl-kubernetes
RUN adduser tpcuser

RUN mkdir -p /var/run/sshd /var/log/supervisor
ADD supervisord.conf /etc/supervisord.conf
