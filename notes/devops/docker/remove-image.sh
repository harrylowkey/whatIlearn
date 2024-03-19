#!/bin/bash

images=$(docker images -q)
if [ -n "$images" ]; then
      docker rmi $images -f
    else
          echo "No Docker images found."
fi
