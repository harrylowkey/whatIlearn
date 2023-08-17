k get ingress -A
k ds ingress -n=<namespace>
k create ingress ingress-pay -n critical-space --rule-"/pay=pay-service:8282" 

