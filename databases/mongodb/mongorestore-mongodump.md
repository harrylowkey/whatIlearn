# Import

```bash
mongorestore --uri "mongodb://root:MegatronSolution2009@localhost:27070" ~/Dev/megatron/pixer_comment/comment/pixerlens-comment-dev/comments.bson
mongorestore --uri "mongodb://root:mongo@localhost:27070" /Users/harrydang/Dev/megatron/renyoo-uat-microservice-dbs/pixer_audit_log_dev/audit_logs.bson
```

# Export

```bash
mongodump --uri "mongodb://root:mongo@localhost:27020" --out="renyoo-uat-microservice-dbs"
```
