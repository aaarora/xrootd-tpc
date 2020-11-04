conf:
	kubectl delete configmap xrootd-single-stream-transfer-script -n osg-services
	kubectl create configmap xrootd-single-stream-transfer-script -n osg-services --from-file=transferScripts/maddash_conf.json --from-file=transferScripts/conf.json --from-file=transferScripts/calcTransferRate.py --from-file=transferScripts/send_to_maddash.py

container:
	kubectl delete -f xrootd-master-single-stream.yaml
	kubectl create -f xrootd-master-single-stream.yaml
