FROM opensciencegrid/software-base:fresh
RUN yum -y install httpd; yum clean all; systemctl enable httpd.service

RUN yum -y install epel-release; yum -y install http://software.internet2.edu/rpms/el7/x86_64/latest/packages/perfSONAR-repo-0.10-1.noarch.rpm; yum -y clean all
RUN yum -y install perfsonar-centralmanagement; yum -y install perfsonar-toolkit; yum -y install supervisor; yum clean all;
RUN mkdir -p /var/run/sshd /var/log/supervisor

ADD maddash.yaml /etc/maddash/maddash-server/
## ADD su /etc/pam.d/
ADD esmondAPI /home/esmondAPI
ADD psconfig.json /home
ADD 10-maddash-server.conf /etc/supervisord.d/10-maddash-server.conf
ADD 10-httpd.conf /etc/supervisord.d/10-httpd.conf

CMD ["/usr/sbin/init"]
