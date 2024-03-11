# Bookmark a volume

We can bookmark a volume within our docker container without mapping it to a file/folder within our local directory.

This can be useful. For an example, our local directory may not have node_modules, but our working directory in our Docker container, /app, does have node_modules folder.

To bookmark a volume within our Docker container, run the following command with this argument.

```bash
docker run -v /app/node_modules -v $(pwd):/app image-id

-v $(pwd):/app: map the current working directory to /app in the container
-v /app/node_modules: bookmark the node_modules volume in the container not the current working directory
```
