# Database Index

- Index is constructed from b-tree

```sql
# excluded the unique indexes
SELECT * FROM pg_indexes
```

```sql
# all the unique indexes
SELECT *
FROM pg_stat_all_indexes
WHERE relname = 'your_table_name';
```
