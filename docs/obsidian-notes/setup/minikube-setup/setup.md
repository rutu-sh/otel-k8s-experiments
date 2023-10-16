
## install docker
---
- [ ] install docker 
	- https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository
- [ ] post installation
	- https://docs.docker.com/engine/install/linux-postinstall/
- [ ] restart the system

## install minikube
---
- [ ] install minikube
	- to start with a 3 node cluster directly, <mark style="background: #FF5582A6;">only follow the steps before `minikube start` in the installation guide. `minikube start` will be used later to setup a three node cluster</mark>.
	- https://minikube.sigs.k8s.io/docs/start/

## install kubectl
---
- [ ] install kubectl
	- https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

## create a three node cluster
---
- [ ] run the following command and copy its logs to a file (number of nodes are optional, you can create a single node cluster as well)
```shell
minikube start --nodes 3 -p otel-learning
```

- [ ] set the minikube profile
```shell
minikube profile otel-learning
```

<mark style="background: #FF5582A6;">NOTE: just doing `minikube stop` will not stop all the clusters. For a proper cleanup always run `minikube delete -all` </mark>

- [ ] list nodes
```shell
kubectl get nodes
```

- [ ] label worker nodes 
```shell
kubectl label node <node_name> node-role.kubernetes.io/worker=worker
```
and list nodes again to verify

- [ ] to ssh into a node
```shell
minikube ssh -n <node_name>
```

- [ ] create a deployment

```shell
kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080
```