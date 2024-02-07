# Export

```bash
pg_dump —file=file-name —format=p —dbnname=db-name —username=db-username —host=db-host —port=db-port
pg_dump --file=renyoo-dev-17-3.sql --format=p --dbname=renyoo-dev --username=root --host=renyoo-dev-rds.cluster-cbshcbhm3sxz.ap-southeast-1.rds.amazonaws.com --port=5432
pg_dump --file=renyoo-dev-microservice-02-02.sql --format=p --dbname=pixerlens_microservices --username=root --host=localhost --port=3432
```


# Import

```bash
psql -h host -U db-user -d db-name < file-name
psql -h renyoo-dev-rds.cluster-cbshcbhm3sxz.ap-southeast-1.rds.amazonaws.com -U root -d renyoo-dev < renyoo-dev-27-02.sql
psql -h localhost -U postgres -d pixerlens-core-dev -p 5432 < renyoo-microservice-02-02.sql
```

# Login

```bash
psql -U db-username -h db-host -p db-port -d db-name
psql -U root -h renyoo-dev-rds.cluster-cbshcbhm3sxz.ap-southeast-1.rds.amazonaws.com -p 5432 -d renyoo-dev
```

