---
title: "Command"
description: "Kubernetes service creation commands: exposing deployments and managing node scheduling"
tags: [kubernetes, kubectl, ckad, services, commands]
---
Create a service that expose the deployment with selector "redis-deployment"

` kubectl expose deployment/redis-deployment --port=6379 --target-port=6379 --name=redis --cluster-ip=`

kubectl uncordon <node-name>
