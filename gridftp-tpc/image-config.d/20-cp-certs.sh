#!/bin/bash                                                                                                                                                                   
CERT_DIR=/etc/grid-security/
if [ -f $CERT_DIR/hostcert.pem ]; then
    cp -f $CERT_DIR/hostcert.pem /root/.globus/hostcert.pem
    cp -f $CERT_DIR/hostkey.pem /root/.globus/hostkey.pem
    chmod 644  /root/.globus/hostcert.pem
    chmod 600 /root/.globus/hostkey.pem
fi
