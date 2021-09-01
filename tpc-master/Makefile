delete:
	- kubectl delete -k ./
create:
	- kubectl apply -k ./
	- kubectl cp tpc $(shell kubectl get pods -l k8s-app=tpc-master -n osg-services -o jsonpath="{.items[0].metadata.name}"):/home/ -n osg-services
