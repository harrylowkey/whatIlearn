- k8s cluster config is stored here: /etc/kubernetes/manifests/

## Shortcut & command tips

1. alias k=kubectl
2. :set expandtab
3. Set context namspace before each question
   - kubectl config set-context <my-context> --namespace=my-namespace

## Command to research again

- kubectl uncordon <node-name>
- kubectl exec webapp(<pod-name>) -- cat /log/app.log
- kubectl explain cronjob.spec.jobTemplate --recursive
- kubectl exec --stdin --tty webapp<pod-name> -- /bin/bash
- kubectl exec -it webapp<pod-name> -- /bin/bash

## Useful comamnds

- kubectl run nginx --image=nginx (pod)
- kubectl run nginx --image=nginx --restart=Never (pod)
- kubectl run nginx --image=nginx --restart=OnFailure (job)
- kubectl run nginx --image=nginx --restart=OnFailure --schedule="\* \* \* \* \*" (job)
- kubectl run nginx --image=nginx --restart=Never --port=80 --namespace=myname --command --serviceaccount=mysa1 --env=HOSSTNAME=local --labels=bu=finance
- kubectl run frontend --replicas=2 --labels=run=load-balancer-example --image=busybox --port=8080 (deployment)
- kubectl expose deployment frontend --type=NodePort --name=frontend-service --port=6262 --target-port=8080
- kubectl set serviceaccount deployment frontend myuser

- kubectl decribe pods | grep --context=10 annotations:
- kubectl describe pods | grep --context=10 Events:
- k get pod --show-labels

## Incoming & Outgoing request

- kubectl exec -it <object-name> -- sh
- nc -v -z -w 2 <service-name> <port-name>
- curl http://"$(minikube ip):$NODE_PORT" # Test request to service
- kubectl get services -l app=kubernetes-bootcamp # Filter service with label
- kubectl run busybox --image=busybox --rm -it --restart=Never --labels=access=granted -- wget -O- http://nginx:80 --timeout 2 # This should be fine
- kubectl run busybox --image=nginx:alpine --rm -it --restart=Never --labels=access=granted -- curl -m 2 http://nginx:80 # This should be fine
