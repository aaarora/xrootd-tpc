FROM opensciencegrid/software-base:fresh

RUN yum -y install vim && \
	yum -y install osg-ca-certs && \
	yum -y install osg-xrootd-standalone && \
	yum -y install x509-scitokens-issuer-client --enablerepo=osg-contrib && \
	yum -y install lcmaps vo-client-lcmaps-voms lcmaps-db-templates osg-configure-misc && \
	yum -y install xrootd-lcmaps vo-client && \
	yum -y install python3

ADD fetch-crl-kubernetes /etc/cron.d/fetch-crl-kubernetes
ADD fix_certs.sh /usr/local/sbin/fix_certs.sh
ADD image-config.d/* /etc/osg/image-config.d/
ADD auth_file /etc/xrootd/auth_file
ADD grid-mapfile /etc/grid-security/grid-mapfile

RUN adduser tpcuser

RUN chown xrootd:xrootd /etc/xrootd/auth_file && \
	chmod 0640 /etc/xrootd/auth_file

RUN mkdir -p /var/log/supervisor
ADD supervisord.conf /etc/supervisord.conf
EXPOSE 8443
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
