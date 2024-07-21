def render_badge_classes(tag):
  tag_class_mapping = {
    'default': 'bg-info text-dark',
    'k8s': 'bg-info text-dark',
    'docker': 'bg-primary',
    'python': 'bg-primary',
    'lock': 'badge-soft-danger',
    'transaction': 'badge-soft-danger',
    'database': 'bg-success',
    'caching': 'bg-success',
    'proxy': 'bg-success',
    'ec2-server': 'bg-warning text-dark',
    'web-development': 'bg-warning text-dark',
    'reverse-proxy': 'badge-soft-danger',
    'aws': 'bg-warning text-dark',
    'redis': 'badge-soft-danger',
    'concurrency': 'bg-success',
    'parallelism': 'bg-warning text-dark',
    'devops': 'bg-warning text-dark',
    'csrf': 'bg-warning text-dark',
    'argocd': 'badge-soft-danger',
    'security': 'badge-soft-danger',
    'helm': 'bg-info text-dark',
  }

  return tag_class_mapping.get(tag, tag_class_mapping['default'])
