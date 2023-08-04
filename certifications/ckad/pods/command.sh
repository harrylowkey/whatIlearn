kubectl set image <object_type>/<object_name> <container_name>=<new_image> # imperative command to update image
kubectl edit pod/pod-name
kubectl replace --force -f file-name # Delete old pod and create new one

kubectl run my-pod --image=nginx --dry-run=client -o yam > pod-definition.yaml # create pod with review and output to file

kubectl delete pods --field-selector=status.phase!=Running # Delete pods that is not running

kubectl get pod pod-name -o yaml > pod-definition.yaml # Output the pod definition to file
kubectl get pods -A // get all pods in all namespace
kubectl get pods -o wide // get pod with IP
kubectl -n <namespace> exec -it <pod-name> -- /bin/sh # Access into pod
kubectl -n <namespace> port-forward <pod-name> 5433(host-port):5432(container-pod) # Forwad pod

