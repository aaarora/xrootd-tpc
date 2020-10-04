FROM opensciencegrid/software-base:fresh

RUN yum -y install vim && \
    yum -y install osg-ca-certs && \
    yum -y install osg-test osg-ca-generator --enablerepo=devops-itb && \
    yum -y install gfal2-plugin-file gfal2-plugin-gridftp && \
    yum -y install globus-gass-copy-progs

RUN easy_install pip && \
    pip install requests 

RUN adduser master
