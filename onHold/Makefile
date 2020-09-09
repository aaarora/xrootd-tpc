#!/bin/bash

kubectl delete configmap xrootd-tpc-conf-https -n osg-services
kubectl create configmap xrootd-tpc-conf-https -n osg-services --from-file=xrootd-third-party-copy.cfg
