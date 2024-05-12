# Setting up a local k8s cluster 


# Setting up a master node

1. install docker ( if you're using linux and are unable to install it due to a 404 on apt-get update, just edit the docker.list to have ubuntu instead of debian: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository), follow post install commands and restart. 
2. install kubeadm, kubectl, kubelet ( https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-kubeadm-kubelet-and-kubectl ) 
3. sudo swapoff -a # otherwise kubeadm won't work
4. kubeadm init --cri-socket=unix:///var/run/cri-dockerd.sock --pod-network-cidr=192.168.0.0/16
5. follow: https://docs.tigera.io/calico/latest/getting-started/kubernetes/quickstart
6. kubeadm token create --print-join-command 

copy the join command and run this on the other node (just copy the command and add `--cri-socket=unix:///var/run/cri-dockerd.sock` to the end of the command)

# Join a new worker node 
1. install docker ( if you're using linux and are unable to install it due to a 404 on apt-get update, just edit the docker.list to have ubuntu instead of debian: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository), follow post install commands and restart. 
2. install kubeadm, kubectl, kubelet ( https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-kubeadm-kubelet-and-kubectl ) 
3. sudo swapoff -a # otherwise kubeadm won't work
4. (paste the join command from the master node, add --cri-socket)

sudo kubeadm join <some-ip> --cri-socket=unix:///var/run/cri-dockerd.sock --token <token> --discovery-token-ca-cert-hash sha256:<hash>


kubeadm join 10.0.0.116:6443 --cri-socket=unix:///var/run/cri-dockerd.sock --token ffi19z.dlvrv12xncg1zb8o --discovery-token-ca-cert-hash sha256:1702cf5a6be0c167a2b21f501fd08a472e500fa114284fc05634fe3960f58320



