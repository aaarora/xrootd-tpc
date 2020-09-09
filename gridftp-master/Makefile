conf:
	kubectl delete configmap gridftp-transfer-script -n osg-services
	kubectl create configmap gridftp-transfer-script -n osg-services --from-file=transferScripts/maddash_conf.json --from-file=transferScripts/conf.json --from-file=transferScripts/calcTransferRate.py --from-file=transferScripts/send_to_maddash.py

container:
	kubectl delete -f gridftp-master.yaml
	kubectl create -f gridftp-master.yaml
