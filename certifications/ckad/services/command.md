k expose deployment/redis-deployment --port=6379 --target-port=6379 --name=redis --cluster-ip=''

- Create a service that expose the deployment with selector "redis-deployment"

kubectl uncordon <node-name>
