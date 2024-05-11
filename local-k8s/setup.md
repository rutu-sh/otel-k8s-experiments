# Setting up a local k8s cluster 


1. install docker
2. install cri-dockerd : sudo dpkg -i cri-dockerd_0.3.13.3-0.ubuntu-jammy_amd64.deb
3. install kubeadm, kubectl, kubelet
4. kubeadm init --cri-socket=unix:///var/run/cri-dockerd.sock --pod-network-cidr=192.168.0.0/16
5. https://docs.tigera.io/calico/latest/getting-started/kubernetes/quickstart
6. kubeadm token create --print-join-command 

copy the join command and run this on the other node (just copy the command and add `--cri-socket=unix:///var/run/cri-dockerd.sock` to the end of the command)


1. sudo kubeadm join <some-ip> --cri-socket=unix:///var/run/cri-dockerd.sock --token <token> --discovery-token-ca-cert-hash sha256:<hash>


For adding a node 

1. Follow the first set of steps till step 3
2. Paste the join command mentioned above 