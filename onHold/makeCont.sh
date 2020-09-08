#!/bin/bash

kubectl delete -f k8s/tpc-ucsd-https.yaml

kubectl create -f k8s/tpc-ucsd-https.yaml
