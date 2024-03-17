kubectl create secret generic <secret-name> --from-literal=<key>=<value>
kubectl get secrets
kubectl describe secrets

echo -n "Secret@123" | base64 
echo -n "cmsdfdf==" | base64 --decoded

