# Setup docker on ec2 server

<!-- published_date: 19 Mar, 2024 -->
<!-- description: command to not to using sudo su to run docker -->
<!-- tags: docker, ec2-server, aws -->

After install docker we need to run command to not to using sudo su to run docker command later

```
chmod 666 /var/run/docker.sock

```
