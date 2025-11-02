# Astro Site Deployment Guide (Server Mode with View Counter)

This guide explains how to deploy the Astro site in server mode to AWS EC2.

## Architecture

- **Mode**: Server-side rendering (SSR) with Node.js
- **Port**: 4321
- **View Counter**: File-based storage using `/view_counts.txt`
- **Deployment**: Docker + Docker Compose on EC2

## Prerequisites

On your EC2 server:
- Docker installed
- Docker Compose installed
- Nginx installed (for reverse proxy)
- Port 4321 accessible (or nginx on port 80/443)

## EC2 Server Setup

### 1. Create docker-compose.yaml

On your EC2 server, create `/home/ubuntu/docker-compose.yaml` (or your preferred location):

```yaml
version: '3.8'

services:
  portfolio-astro:
    image: ${ECR_REGISTRY}/portfolio-astro:latest
    container_name: portfolio-astro
    restart: unless-stopped
    ports:
      - "4321:4321"
    environment:
      - NODE_ENV=production
      - HOST=0.0.0.0
      - PORT=4321
    volumes:
      - ./view_counts.txt:/view_counts.txt
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:4321"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### 2. Initialize view_counts.txt

Create an empty view counts file:

```bash
touch view_counts.txt
```

### 3. Setup Nginx Reverse Proxy (Optional but Recommended)

Create `/etc/nginx/sites-available/astro`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:4321;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }
}
```

Enable the site:

```bash
sudo ln -s /etc/nginx/sites-available/astro /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### 4. Configure Docker Login

Login to your Docker registry:

```bash
echo "YOUR_DOCKER_PASSWORD" | docker login --username YOUR_USERNAME --password-stdin
```

## GitHub Actions Deployment

The deployment is automated via GitHub Actions (`.github/workflows/astro.yaml`):

### What it does:

1. **Build Stage**:
   - Checks out code
   - Builds Docker image with Astro server
   - Pushes to Docker registry

2. **Deploy Stage**:
   - SSHs to EC2 server
   - Backs up current `view_counts.txt`
   - Pulls new Docker image
   - Updates docker-compose.yaml with new image tag
   - Restarts container
   - Restores `view_counts.txt` to new container

### Required GitHub Secrets:

Set these in your GitHub repository settings:

- `DOCKER_HUB_USERNAME`: Docker Hub username
- `DOCKER_HUB_PASSWORD`: Docker Hub password/token
- `ECR_REGISTRY`: Your Docker registry (e.g., `username` for Docker Hub)
- `SSH_HOST`: EC2 public IP or domain
- `SSH_USER`: EC2 username (usually `ubuntu`)
- `SSH_KEY`: EC2 private SSH key

## View Counter Persistence

The view counter data is stored in `/view_counts.txt` in the format:

```
index:10
projects:5
notes:3
notes/backend/caching/caching-strategies:2
```

### Data Persistence Strategy:

1. **Volume Mount**: `view_counts.txt` is mounted as a volume in docker-compose
2. **Deployment Backup**: GitHub Actions backs up the file before deployment
3. **Restore**: File is restored to the new container after deployment

### Manual Backup:

```bash
# Backup from container
docker cp portfolio-astro:/view_counts.txt ./view_counts_backup.txt

# Restore to container
docker cp ./view_counts_backup.txt portfolio-astro:/view_counts.txt
```

## Testing Locally

Test the Docker setup locally:

```bash
cd astro-site

# Build
docker build -t portfolio-astro:local .

# Run
docker run -p 4321:4321 -v $(pwd)/../view_counts.txt:/view_counts.txt portfolio-astro:local

# Visit http://localhost:4321
```

## Troubleshooting

### View counter not updating:

```bash
# Check container logs
docker logs portfolio-astro

# Check if API endpoints are working
curl -X POST http://localhost:4321/api/views/test
curl http://localhost:4321/api/views/test

# Check file permissions
docker exec portfolio-astro ls -la /view_counts.txt
```

### Container not starting:

```bash
# Check logs
docker logs portfolio-astro

# Check if port is already in use
sudo lsof -i :4321

# Restart container
docker-compose restart portfolio-astro
```

### View counts lost after deployment:

The GitHub Actions workflow should automatically backup and restore. If not:

```bash
# Restore from backup
docker cp ./view_counts.txt portfolio-astro:/view_counts.txt
docker-compose restart portfolio-astro
```

## Monitoring

Check if the site is running:

```bash
# Health check
curl http://localhost:4321

# Container status
docker ps | grep portfolio-astro

# View logs
docker logs -f portfolio-astro
```

## Updating

Deployments are automatic on push to master branch. To manually deploy:

1. Push changes to master branch
2. GitHub Actions will automatically build and deploy
3. View counts are preserved automatically

## Port Information

- **Application**: 4321 (Node.js server)
- **Nginx**: 80/443 (reverse proxy to 4321)
- **API Endpoints**: Available at `/api/views/{path}`
