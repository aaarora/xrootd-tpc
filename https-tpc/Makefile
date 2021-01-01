conf: 
	kubectl delete configmap xrootd-tpc-https -n osg-services
	kubectl create configmap xrootd-tpc-https -n osg-services --from-file=xrootd-third-party-copy.cfg

cagen-conf:
	kubectl delete configmap cagen-script-modified -n osg-services
	kubectl create configmap cagen-script-modified --from-file=/home/aaarora/osg-ca-generator/lib/cagen.py -n osg-services

ca-secret:
	kubectl delete secret https-self-certs -n osg-services
	kubectl create secret generic https-self-certs --from-file=/home/aaarora/openssl-gencerts/OSG-Test-CA.pem -n osg-services

