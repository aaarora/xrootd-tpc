#!/bin/bash

kubectl delete -f k8s/tpc-ucsd.yaml
kubectl delete -f k8s/tpc-kans.yaml
kubectl delete -f k8s/tpc-chic.yaml

#kubectl create -f k8s/tpc-ucsd.yaml
#kubectl create -f k8s/tpc-kans.yaml
#kubectl create -f k8s/tpc-chic.yaml
