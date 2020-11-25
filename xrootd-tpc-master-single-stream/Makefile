conf:
	kubectl delete configmap xrootd-transfer-script-single-stream -n osg-services
	kubectl create configmap xrootd-transfer-script-single-stream -n osg-services --from-file=transferScripts/maddash_conf.json --from-file=transferScripts/conf.json --from-file=transferScripts/calcTransferRate.py --from-file=transferScripts/send_to_maddash.py

container:
	kubectl delete -f xrootd-master-single-stream.yaml
	kubectl create -f xrootd-master-single-stream.yaml
