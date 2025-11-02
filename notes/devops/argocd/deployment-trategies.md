---
title: "ArgoCD: Deployment strategies"
description: "ArgoCD: Deployment strategies"
tags:
  - devops
  - argocd
---

- *Default* Rolling Updates (suitable for development CD): Use when you need a balance between zero downtime and minimal complexity, and when incremental updates suffice.
- Definition: Rolling updates gradually replace old versions of the application with new versions without downtime.
- How It Works:
    - New pods are incrementally deployed, and old pods are terminated as the new ones become ready.
    - This ensures that a specified number of instances of the application are always running during the update process.
- Benefits:
    - Minimal Downtime: Ensures continuous availability of the application during the update.
    - Progressive Rollout: Changes are applied incrementally, allowing for early detection of issues.
    - Kubernetes Native: Utilizes native Kubernetes deployment strategies, making it seamless for Kubernetes environments.


- Blue/Green Deployment (suitable for development CD): Use for significant updates or when you need to validate a new version in a production-like environment before going live.
- Canary Deployment (suitable for **production** CD): Use for high-risk environments where you want to gradually introduce changes and gather feedback.
- Recreate Deployment: Use for applications that can handle downtime or need complete resets.
