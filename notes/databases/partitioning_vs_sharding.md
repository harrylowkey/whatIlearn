---
title: "Partitioning vs Sharding"
description: "Partitioning vs Sharding"
tags:
  - database
  - partition
  - shard
---
Database partitioning, sharding, and replication are techniques used to manage data in a database to improve performance, scalability, and availability. Here's an overview of each:

### Database Partitioning

- One database
    - Horizontal partitioning: by rows
    - Vertical partitioning: by columns

Partitioning involves dividing a large database into smaller, more manageable pieces called partitions. Each partition can be managed and accessed separately,
which can improve performance and manageability. Partitioning can be done in several ways:

1. **Horizontal Partitioning (Range Partitioning)**: Rows are divided into different tables based on a range of values.
For example, a table with sales data could be partitioned by date, with each partition containing data for a specific month or year.

2. **Vertical Partitioning**: Columns are divided into different tables. For example, a customer table could be split into two tables: 
- one containing frequently accessed columns like customer IDs and names, 
- and another with less frequently accessed information like addresses and phone numbers.

3. **List Partitioning**: Data is divided based on a list of values. For example, a table of products might be partitioned based on product categories.

4. **Hash Partitioning**: A hash function is applied to a key to determine the partition in which to place the row. This can help evenly distribute data across partitions.

### Sharding

- Large dataset across mulitple databases or servers
- Sharding is one of the implemenation of Horizontal Partitioning

Example:
    - Geo-based sharding: user location
    - Range-based sharding: user ID
    - Hash-based sharding
    - Manual and automatic sharding

Sharding is a type of horizontal partitioning, but it involves splitting a *large dataset across multiple databases or servers*, known as shards.
Each shard holds a subset of the data, and together they form the complete dataset.
Sharding can improve performance and scalability, as queries can be executed in parallel across shards. There are different approaches to sharding:

1. **Key-Based Sharding (Hash Sharding)**: A hash function is used to determine the shard placement based on a shard key. This method helps distribute data evenly but can be complex to implement.

2. **Range-Based Sharding**: Data is divided into shards based on ranges of a key. This can be simpler to implement but may lead to uneven data distribution if the data is not uniformly distributed.

3. **Geographic Sharding**: Data is partitioned based on geographic location, which can be useful for applications with users distributed across different regions.

### Replication

- Copying data from one database to another

Replication involves copying data from one database to another to ensure high availability and fault tolerance. There are different types of replication:

1. **Master-Slave Replication**: One database (the master) receives all write operations, and changes are replicated to one or more read-only databases (slaves).
This setup can improve read performance and provide redundancy.

2. **Master-Master Replication**: Multiple databases (masters) can accept write operations, and changes are replicated between them.
This can provide high availability and allow for distributed writes but requires conflict resolution mechanisms.

3. **Multi-Master Replication**: Similar to master-master replication but involves more than two databases, providing even greater redundancy and availability.

4. **Synchronous vs. Asynchronous Replication**: In synchronous replication, changes are replicated immediately, ensuring consistency but potentially slowing down write operations.
In asynchronous replication, changes are propagated after a delay,which can improve performance but might lead to temporary inconsistencies.

These techniques can be used individually or in combination, depending on the specific needs and architecture of the database system.
