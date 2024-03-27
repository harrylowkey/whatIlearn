def render_badge_classes(tag):
  tag_class_mapping = {
    'k8s': 'bg-info text-dark',
    'docker': 'bg-primary',
    'python': 'badge-soft-danger',
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
    'default': 'bg-dark',
  }

  return tag_class_mapping.get(tag, tag_class_mapping['default'])
