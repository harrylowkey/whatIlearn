# Useful Commands
- k8s cluster config is stored here: /etc/kubernetes/manifests/

## Shortcut & command tips

1. alias k=kubectl
2. :set expandtab
3. Set context namspace before each question
   - kubectl config set-context <my-context> --namespace=my-namespace

## Command to research again

- kubectl uncordon <node-name>
- kubectl explain cronjob.spec.jobTemplate --recursive
- kubectl exec --stdin --tty webapp<pod-name> -- /bin/bash

## Create pod/deploy/service comamnds

- kubectl run nginx --image=nginx (pod)
- kubectl run nginx --image=nginx --restart=Never (pod)
- kubectl run nginx --image=nginx --restart=OnFailure (job)
- kubectl run nginx --image=nginx --restart=OnFailure --schedule="\* \* \* \* \*" (job)
- kubectl run nginx --image=nginx --restart=Never --port=80 --namespace=myname --command --serviceaccount=mysa1 --env=HOSSTNAME=local --labels=bu=finance

- kubectl create deploiy frontend --replicas=2 --labels=run=load-balancer-example --image=busybox --port=8080 (deployment)
- kubectl expose deployment frontend --type=NodePort --name=frontend-service --port=6262 --target-port=8080 (service)

- kubectl set serviceaccount deployment frontend myuser

### Describe object

- kubectl decribe pods | grep --context=10 annotations:
- kubectl describe pods | grep --context=10 Events:
- k get pod --show-labels

## Get log, filter objects

- kubectl exec webapp(<pod-name>) -- cat /log/app.log
- kubectl get <objects>(pod, deploy, svc) -l app=kubernetes-bootcamp # Filter service with label

## Incoming & Outgoing request

- kubectl exec -it <object-name> -- sh
- nc -v -z -w 2 <service-name> <port-name>

## How to check if deployment success or fail

Note: 
- image:alpine has curl not
- image:busybox do not has curl

Scenario: we create a deployment with image `nginx` then expose it as a ClusterIP service --port=8001 --target-port=80
<!-- (need to point to this port because to test nginx we need to access to it) -->
<!-- in the case we deploy backend run on port 3000, so we need to add --target-port=3000 (container-port) --port=... (it is the service port that other services in the same cluster will use) -->

### Test request to service with type NodePort
- Expose service with type=NodePort
- Get node IP: k get nodes -owide
- Execute to a deploy or pod in the same cluster
- curl NODE_IP:NODE_PORT(NodePort defined in service)" # Test request to service

### Test request to pod
- kubectl get pod -owide
- then take the pod IP
- kubectl run busybox --image=nginx:alpine --rm -it --restart=Never -- curl -m 2 <pod-ip>(:80)
- kubectl run busybox --image=busybox --rm -it --restart=Never -- wget -O- (http://)<pod-name>:80 --timeout 2 # (test curl to pod)

### Test request to service with type ClusterIp
- kubectl run busybox --image=nginx:alpine --rm -it --restart=Never -- curl -m 2 ClusterIP:<service-port>(...:8001)
- kubectl run busybox --image=nginx:alpine --rm -it --restart=Never -- curl -m 2 (http://)<service-name>:<service-port>(service-name:8001)
- k expose <deployment-name> --port=<service-port> --target-port=<container-port-that-we-want-to-redirect-request-to>

## Forward port from service to local

kubectl port-forward svc/my-service <local-port>:<service-port> # listen on local port 5000 and forward to Service target port with name <my-service-port>
kubectl port-forward svc/my-service 5000:5000 # listen on local port 5000 and forward to port 5000 on Service backend
kubectl port-forward deploy/my-deployment 5000:6000

> We should forward svc to pulic access, not pod

>In Kubernetes, when you want to expose an application to the external world, you generally do it through a Service rather than directly exposing a Pod's port. Here's why:

>Abstraction and Decoupling:
>A Service provides an abstraction layer that decouples the Pod (running your application) from the way it's accessed. This allows you to make changes to your Pods without affecting how clients connect to your application.

>Load Balancing:
>Services provide load balancing across multiple Pods. If you have multiple replicas of your application running, a Service will distribute the incoming traffic among them, helping to achieve high availability and scalability.

>Service Types:
>Services in Kubernetes come with different types, such as ClusterIP (only accessible within the cluster), NodePort (exposes the service on a specific port on all nodes in the cluster), and LoadBalancer (provisions an external load balancer in a cloud environment).

>Security:
>Exposing a Pod directly might not be the best practice from a security standpoint. A Service allows you to control and secure the access to your application.
>Dynamic IP and DNS Management:

>Services are assigned a stable IP address and DNS name within the cluster. This makes it easier for clients to discover and connect to your application.
>Here's an example of how you might expose a Pod using a Service:

### Copy file to and from containers

kubectl cp /tmp/foo_dir my-pod:/tmp/bar_dir # Copy /tmp/foo_dir local directory to /tmp/bar_dir in a remote pod in the current namespace
kubectl cp /tmp/foo my-pod:/tmp/bar -c my-container # Copy /tmp/foo local file to /tmp/bar in a remote pod in a specific container
kubectl cp /tmp/foo my-namespace/my-pod:/tmp/bar # Copy /tmp/foo local file to /tmp/bar in a remote pod in namespace my-namespace
kubectl cp my-namespace/my-pod:/tmp/foo /tmp/bar # Copy /tmp/foo from a remote pod to /tmp/bar locally

