conf:
	-kubectl delete configmap tpc-script -n osg-services
	-kubectl create configmap tpc-script -n osg-services \
	--from-file=transferScripts/gftp-cron \
	--from-file=transferScripts/https-cron \
	--from-file=transferScripts/doTransfer \
	--from-file=transferScripts/maddash_conf.json \
	--from-file=transferScripts/conf.json \
	--from-file=transferScripts/calcTransferRate \
	--from-file=transferScripts/sendToMaddash

container:
	-kubectl delete -f tpc-master.yaml
	-kubectl create -f tpc-master.yaml
