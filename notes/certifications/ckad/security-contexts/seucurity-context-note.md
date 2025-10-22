---
title: "Seucurity Context Note"
description: "Kubernetes security contexts: container-level overrides pod-level, default user is root if not specified"
tags: [kubernetes, security, ckad, security-context, pod-security]
---
securityContext in container will override the securityContext in pod
if not defined runAsUser -> it means we're running as root user
