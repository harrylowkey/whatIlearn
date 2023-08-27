# Check Access
kubectl auth can-i create deployments --as dev-user
kubectl auth ca-i delete notes --as dev-user --namsepace test
