# Docker command

```bash
docker run -d --name "my_container" -e "ENV_VARIABLE1=VALUE1" -e "ENV_VARIABLE2=VALUE2" -p HOST_PORT:CONTAINER_PORT my_image_name
```

```bash

docker run -d --name "mongo" -e "MONGO_INITDB_ROOT_USERNAME=root" -e "MONGO_INITDB_ROOT_PASSWORD=mongo" -p 27017:27017 mongo
docker run -d --name "postgres-11" -e "POSTGRES_USER=postgres" -e "POSTGRES_PASSWORD=postgres" -p 5432:5432 postgres:11
docker run -d --name "postgis-11" -e "POSTGRES_USER=postgres" -e "POSTGRES_PASSWORD=postgres" -p 5432:5432 postgis/postgis:11-3.3
```
