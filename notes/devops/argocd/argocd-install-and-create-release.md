<!-- published_date: 01 Jul, 2024 -->
<!-- description: Install argocd & create release -->
<!-- tags: devops, argocd, helm -->

# Deployment

## Install/upgrade release with helm chart public repo

1. Add helm repo
`helm repo add argocd https://argoproj.github.io/argo-helm`

2. Install/upgrade the chart
`helm upgrade argocd argocd/ --namespace argocd --install`

## Install/upgrade release with helm chart config file
.
└── argocd/
    ├── Chart.lock
    ├── Chart.yaml
    └── values.yaml

1. Build dependencies if needed
`helm dependency build infrastructures/database`

2. Install/upgrade the chart
`kc ns argocd`
`helm upgrade argocd argocd/ --namespace argocd --install -f argocd/values.yaml`

