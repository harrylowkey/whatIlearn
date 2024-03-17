# AWS ECR docker login
aws ecr get-login-password --region ap-southeast-1 --profile=renyoo-eks | docker login --username AWS --password-stdin 276736272121.dkr.ecr.ap-southeast-1.amazonaws.co
