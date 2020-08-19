FROM opensciencegrid/software-base:fresh

RUN yum -y install vim && \
    yum -y install osg-ca-certs && \
    yum -y install osg-xrootd-standalone && \
    yum -y install gfal2-util gfal2-plugin-http && \
    yum -y install python3

ADD fetch-crl-kubernetes /etc/cron.d/fetch-crl-kubernetes
ADD fix_certs.sh /usr/local/sbin/fix_certs.sh
RUN adduser tpcuser

RUN mkdir -p /var/run/sshd /var/log/supervisor
ADD supervisord.conf /etc/supervisord.conf
EXPOSE 8080
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
