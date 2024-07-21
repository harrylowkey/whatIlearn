<!-- published_date: 01 Jul, 2024 -->
<!-- description: ArgoCD: Declarative deployment with helm -->
<!-- tags: devops, argocd, helm -->

# Helm Deployment Steps

## Installation 

- Create/config kubernetes cluster
- [Install helm](https://helm.sh/docs/intro/install/) 
- [Install argocd using helm chart](./deploy-with-helm.md)
 

## Declarative deployment
```
.
├── applications/
│   └── test-project.yaml
├── infrastructures/
│   └── helm-charts/
│       ├── templates/
│       │   ├── deployment.yaml
│       │   ├── service.yaml
│       │   └── ...
│       └── Chart.yaml
└── enviroments/
    └── test-prject/
        └── backend.yaml
```

1. Define template files in `infrastructures/helm-charts/templates/`

2. Config values in `enviroments/test-prject/backend.yaml`

3. Create `test` project/application

```yaml
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: test
  namespace: argocd
spec:
  clusterResourceWhitelist:
    - group: '*'
      kind: '*'
  destinations:
    - namespace: test
      server: https://kubernetes.default.svc
  orphanedResources:
    warn: false
  sourceRepos:
    - '*'
---
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: backend
  namespace: argocd
spec:
  project: test
  source:
    repoURL: 'git@github.com:*github-username*/*github-repo-name*.git'
    path: infrastructures/helm-charts
    targetRevision: develop
    helm:
      valueFiles:
        - /environments/test-prject/backend.yaml
  destination:
    server: 'https://kubernetes.default.svc'
    namespace: test
  syncPolicy:
    automated: {}
    syncOptions:
      - CreateNamespace=true
```

2. Sync application
`k apply -f applications/test-project.yaml`
