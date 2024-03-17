kubectl exec -it kube-apiserver-controlplane -n kube-system -- kube-apiserver -h | grep 'enable-admission-plugins'

- To enable/disbale admission plugin for k8s:
1. vim /etc/kubernetes/manifests/kube-apiserver.yaml
2. - --enable-admission-plugins=NodeRestriction,NamespaceAutoProvision
3. - --disable-admission-plugins=DefaultStorageClass
