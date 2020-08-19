#!/bin/bash

kubectl delete -f k8s/svc/ucsd-svc.yaml -n osg-services
kubectl delete -f k8s/svc/kans-svc.yaml -n osg-services
kubectl delete -f k8s/svc/chic-svc.yaml -n osg-services

kubectl create -f k8s/svc/ucsd-svc.yaml -n osg-services
kubectl create -f k8s/svc/kans-svc.yaml -n osg-services
kubectl create -f k8s/svc/chic-svc.yaml -n osg-services
