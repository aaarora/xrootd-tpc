FROM opensciencegrid/software-base:fresh

RUN yum -y install vim && \
    yum -y install osg-xrootd-standalone --enablerepo=osg-upcoming-development

RUN adduser tpcuser
ADD supervisord.conf /etc/supervisord.d/10-xrootd-http.conf
