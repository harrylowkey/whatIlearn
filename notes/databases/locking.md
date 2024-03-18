# Acquire Lock

<!-- published_date: 18 Mar, 2024 -->
<!-- description: Note for locking -->
<!-- tags: database, lock -->

1. Acquire FOR UPDATE lock

- This lock is typically used when a transaction intends to make changes to the data.
  It prevents other transactions from acquiring a conflicting lock (FOR UPDATE or FOR SHARE) on the same data
  until the transaction that acquired the FOR UPDATE lock is committed or rolled back.

2. Acquire FOR SHARE lock

- This lock is often referred to as a "shared lock" or a "read lock."
  It is used when a transaction wants to read the data but does not intend to modify it.
  It allows multiple transactions to acquire a FOR SHARE lock on the same data simultaneously, allowing concurrent reads.

- Other transactions can still read the data or acquire a FOR SHARE lock as well.

# Relationship betweeb Lock and Transaction

- Acquire lock are using in the transaction to control the data access
- Acquire locks can be different in different **transaction isolation levels**

## Some use cases

1. READ UNCOMMITTED Isolation Level

- Transaction 1:
  Acquires a FOR UPDATE lock on row 1.
- Transaction 2 (READ UNCOMMITTED):
  Wants to read data from row 1. <br>
  Behavior: Transaction 2 is not blocked by Transaction 1's FOR UPDATE lock. READ UNCOMMITTED allows dirty reads, so Transaction 2 can read uncommitted data.

2. READ COMMITTED Isolation Level

- Transaction 1:
  Acquires a FOR UPDATE lock on row 1.
- Transaction 2 (READ COMMITTED):
  Wants to read data from row 1. <br>
  Behavior: Transaction 2 is not blocked by Transaction 1's FOR UPDATE lock. It can read the uncommitted data.

3. REPEATABLE READ Isolation Level

- Transaction 1:
  Acquires a FOR UPDATE lock on row 1.
- Transaction 2 (REPEATABLE READ):
  Wants to read data from row 1. <br>
  Behavior: Transaction 2 is blocked by Transaction 1's FOR UPDATE lock. <br>
  REPEATABLE READ prevents non-repeatable reads but not phantom reads, so Transaction 2 waits until Transaction 1 completes.

4. SERIALIZABLE Isolation Level

- Transaction 1:
  Acquires a FOR UPDATE lock on row 1.
- Transaction 2 (SERIALIZABLE):
  Wants to read data from row 1. <br>
  Behavior: Transaction 2 is blocked by Transaction 1's FOR UPDATE lock. SERIALIZABLE provides the strictest isolation, blocking reads by default until writes are completed.
