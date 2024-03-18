# Database Index

- Index is constructed from b-tree


1. excluded the unique indexes
> ```
> SELECT * FROM pg_indexes
> ```

2. Get all the unique indexes
>```
>SELECT *
>FROM pg_stat_all_indexes
>WHERE relname = 'your_table_name';
>```
