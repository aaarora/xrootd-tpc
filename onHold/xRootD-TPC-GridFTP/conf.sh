#!/bin/bash

kubectl delete configmap xrootd-tpc-conf -n osg-services
kubectl create configmap xrootd-tpc-conf -n osg-services --from-file=xrootd-third-party-copy.cfg

