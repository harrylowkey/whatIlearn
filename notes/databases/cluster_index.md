---
title: "Cluster Index"
description: "Understanding clustered indexes: data storage order, one-per-table limitation, and optimal use cases for range queries"
tags:
  - database
  - indexing
  - clustered-index
  - performance
  - query-optimization
---
## Key Points
- Data Stored in Index Order: A clustered index sorts and stores the data rows of the table based on the values of the indexed column(s). Therefore, the index and the actual data rows are stored together, making the table itself the index.
- One Clustered Index per Table: Since the clustered index controls the physical order of data in the table, you can only have one clustered index per table. The data can only be stored in one order at a time.
- Efficient for Range Queries: Clustered indexes are particularly efficient for queries that return a range of values (e.g., retrieving data between two dates), as the data is already sorted, and the database doesn't need to scan the entire table.
- Primary Key Often Used: By default, in most relational databases, the primary key of a table is implemented as a clustered index (though you can explicitly define a different clustered index). If the primary key is clustered, the data will be stored in the order of the primary key values.


## When to Use a Clustered Index:

- When the table is primarily queried based on ranges (e.g., date ranges, sequential numeric IDs).
- When the table's primary key is a column with unique values that grow sequentially (e.g., an auto-incrementing ID).
- When you want faster performance on queries involving ORDER BY clauses on the indexed column.


