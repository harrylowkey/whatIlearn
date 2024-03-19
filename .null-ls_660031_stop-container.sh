#!/bin/bash
#
containers=$(docker ps -q)
if [ -n "$containers" ]; then
    docker stop $containers
else
    echo "No running containers found."
fi
