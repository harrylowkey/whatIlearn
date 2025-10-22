---
title: "Best practices"
description: "Docker Dockerfile best practices: prefer COPY over ADD, with exceptions for downloads and archive extraction"
tags: [docker, dockerfile, best-practices, devops, containers]
---
## Prefer COPY over ADD
Prefer COPY over ADD when copying files from a location to a Docker image.

Use ADD to:
- download external files
- extract an archive to the destination

https://pbs.twimg.com/media/GH6RsL0W0AESCf3?format=jpg&name=large
