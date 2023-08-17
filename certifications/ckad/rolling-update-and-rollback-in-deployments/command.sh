kubectl rollout status deployment/myapp-deployment
kubectl rollout history deployment/myapp-deployment --revision=n
kubectl rollout undo deployment nginx --to-revision=1
kubectl describe deployments. nginx | grep -i image:
