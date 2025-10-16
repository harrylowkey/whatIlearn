---
title: "Optimistic Locking vs Pessimistic Locking"
description: "Note for locking"
tags:
  - database
  - lock
---
https://medium.com/@abhirup.acharya009/managing-concurrent-access-optimistic-locking-vs-pessimistic-locking-0f6a64294db7

🔑 Key Characteristics of Pessimistic Locking:

- Acquiring Locks Upfront: Before performing any read or write operation on a resource, pessimistic locking acquires locks on the resource to prevent other concurrent transactions from accessing it concurrently.

- Exclusive Access: Once a lock is obtained, it grants exclusive access to the locked resource to the transaction that holds the lock. Other transactions must wait until the lock is released before they can access the resource.

- Potential for Waiting: Since locks are held for the entire duration of a transaction, there might be waiting times for other transactions if they request access to the locked resource.

- Different Granularities: Pessimistic locking can operate at various granularities, such as database-level locks, table-level locks, row-level locks, or even finer-grained locks at the column level.

🔑 Key Concepts of Optimistic Locking

- Validation Before Commit: Rather than preventing concurrent access, optimistic locking defers conflict detection until the time of committing changes. It allows transactions to proceed independently and optimistically assumes that conflicts won’t arise during the execution phase.

- Validation at Commit Time: Before committing changes, the system checks whether any other transaction has modified the resource since the current transaction started. This validation is typically done by comparing versions or timestamps associated with the resource.

- Handling Conflicts: If conflicts are detected during the validation phase (e.g., if another transaction modified the resource), the system takes appropriate action. This could involve rolling back the current transaction or retrying it to incorporate the latest changes.

## Acquire Lock


1. Acquire FOR UPDATE lock (Pessimistic Locking)

- This lock is typically used when a transaction intends to make changes to the data.
  It prevents other transactions from acquiring a conflicting lock (FOR UPDATE or FOR SHARE) on the same data
  until the transaction that acquired the FOR UPDATE lock is committed or rolled back.

2. Acquire FOR SHARE lock (Optimistic Locking)

- This lock is often referred to as a "shared lock" or a "read lock."
  It is used when a transaction wants to read the data but does not intend to modify it.
  It allows multiple transactions to acquire a FOR SHARE lock on the same data simultaneously, allowing concurrent reads.

- Other transactions can still read the data or acquire a FOR SHARE lock as well.

# Relationship betweeb Lock and Transaction

- Acquire lock are using in the transaction to control the data access
- Acquire locks can be different in different **transaction isolation levels**
