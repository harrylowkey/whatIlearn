---
title: "Query Optimization Tips"
---
## Condition in Join And Where

### 1. **`INNER JOIN` with Condition vs `WHERE` with Condition**

When you use an `INNER JOIN` with a condition, it acts as a filter within the join itself. This means only rows that meet the join condition (and the additional condition) are combined and included in the result set.

For example:
```sql
SELECT *
FROM TableA A
INNER JOIN TableB B ON A.id = B.id AND B.value > 10
```

In this case, only rows where `A.id = B.id` and `B.value > 10` will be included in the result set. Here, the filter `B.value > 10` is applied during the join operation.

Alternatively, using `WHERE`:
```sql
SELECT *
FROM TableA A
INNER JOIN TableB B ON A.id = B.id
WHERE B.value > 10
```

Here, all rows that satisfy `A.id = B.id` are joined first, and then `B.value > 10` is applied to filter the joined result set. 

In terms of result, both examples may return the same output, but their internal operations could differ depending on the SQL optimizer. In general:
- **Using `JOIN` conditions** can sometimes lead to more efficient execution plans because the filtering happens as part of the join process.
- **Using `WHERE` conditions** applies filtering after the join is completed, which might result in more data being processed during the join phase.

### 2. **`LEFT JOIN` with Condition vs `WHERE` with Condition**

With `LEFT JOIN`, there’s a bigger difference. A `LEFT JOIN` includes all rows from the left table, even if there’s no match in the right table.

For example:
```sql
SELECT *
FROM TableA A
LEFT JOIN TableB B ON A.id = B.id AND B.value > 10
```

In this case, all rows from `TableA` are returned, but rows from `TableB` are only included if both `A.id = B.id` and `B.value > 10` are true. If there’s no match or if `B.value` is not greater than 10, columns from `TableB` will show as `NULL` for that row.

However, with `WHERE`:
```sql
SELECT *
FROM TableA A
LEFT JOIN TableB B ON A.id = B.id
WHERE B.value > 10
```

Here, the `WHERE` clause is applied **after** the `LEFT JOIN`, which turns it into an **`INNER JOIN`-like filter** because rows where `B.value <= 10` or `B.value IS NULL` are excluded. The effect is that only rows where there’s a match in `TableB` and `B.value > 10` will be returned, which changes the logic from a `LEFT JOIN` to something similar to an `INNER JOIN`.

### 3. **Performance Considerations**

- **Applying conditions within the `JOIN`** (especially for `INNER JOIN`) can sometimes be more efficient, as it reduces the amount of data processed after the join.
- **Using `WHERE` conditions** after the join may lead to a more complex execution plan, especially if it involves filtering data that could have been limited earlier in the join.

### Summary

- **`INNER JOIN` with condition** and `WHERE` with condition may yield the same results but can differ in efficiency.
- **`LEFT JOIN` with condition** and `WHERE` with condition can produce **different results**. Using a condition in `WHERE` after a `LEFT JOIN` can unintentionally filter out rows and make it behave like an `INNER JOIN`.
- **Performance** can vary depending on whether conditions are applied in the `JOIN` clause or in the `WHERE` clause.

For the most efficient query, it’s generally recommended to put conditions directly within the `JOIN` clause if you only want rows that meet specific criteria, especially for `INNER JOIN`. For `LEFT JOIN`, be careful with conditions in the `WHERE` clause, as they can unintentionally filter out rows.
