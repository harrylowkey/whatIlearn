kubectl get cm
kubectl create cm config-map-name --from-literal=APP_COLOR=blue \
                                  --from-literal=APP_NAME=Macbook
