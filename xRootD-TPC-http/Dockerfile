FROM opensciencegrid/software-base:fresh

RUN yum -y install vim && \
    yum -y install osg-ca-certs && \
    yum -y install osg-xrootd-standalone && \
    yum -y install openssl openssh-server openssh-clients

ADD fetch-crl-kubernetes /etc/cron.d/fetch-crl-kubernetes
ADD fix_certs.sh /usr/local/sbin/fix_certs.sh

RUN mkdir -p /root/.ssh; \
    chmod 700 /root/.ssh; \
    mkdir -p /var/run/sshd; \
    chmod 700 /var/run/sshd; \
    sed -i "s/GSSAPIAuthentication yes/GSSAPIAuthentication no/" /etc/ssh/sshd_config; \
    /usr/sbin/sshd-keygen; \
    ssh-keygen -q -t dsa -f /root/.ssh/id_dsa -N '' -C 'keypair generated during docker build' && cat /root/.ssh/id_dsa.pub > /root/.ssh/authorized_keys; \
    chmod 600 /root/.ssh/authorized_keys;

RUN adduser tpcuser

RUN mkdir -p /var/run/sshd /var/log/supervisor
ADD supervisord.conf /etc/supervisord.conf
EXPOSE 8080 1024
