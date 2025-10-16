---
title: "Setup docker on ec2 server"
description: "command to not to using sudo su to run docker"
---
<!-- tags: aws, docker, ec2-server -->

After install docker we need to run command to not to using sudo su to run docker command later

```
chmod 666 /var/run/docker.sock

```
