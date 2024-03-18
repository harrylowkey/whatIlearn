# Transactions

<!-- published_date: 18 Mar, 2024 -->
<!-- description: Isolation levels vs read phenomena -->
<!-- tags: database, transaction -->

## Read phenomena

- Dirty reads
- Non-repeatable reads
- Phantom reads

## Isolation levels

### Read Uncommitted

Other transactions can access and update same data. But in the level, it will read the data that has been changed but has not committed yet

---

- let a = 1
- Transaction 1: update a -> 2 (not commit yet)
- Transaction 2: read a -> 2
- Transaction 1: failed -> rollback -> a = 1
- Transaction 2: increment a + 1 -> a = 2 + 1 = 3
- => not correct

---

### Read Committed

Other transactions can access and update same data. But in the level, if re-read same data can cause `Non-repeatable Read`

- In the Read Committed isolation level, transactions are allowed to access and update the same data concurrently. However, the key point is that a transaction reading data will only see changes committed by other transactions. It won't read uncommitted changes, preventing what is known as "dirty reads."
- Breakdowns:

  - **Reads:** Transactions can read data that has been committed by other transactions.
  - **Updates:** Transactions can also update data, and those updates become visible to other transactions only after they are committed.
  - **Dirty Reads:** Dirty reads, where a transaction reads uncommitted changes made by another transaction, **_are not allowed_**.

---

- let a = 1
- Transaction 1: update a -> 2 (not commit yet)
- Transaction 2: read a -> 1 (only read committed data)
- Transaction 1: commit -> a = 2
- (Case 1) Transaction 2: read a **again** -> a = 2
- => Non-repeatable Read
- (Case 2) Transaction 2: increment a = a + 1 = 1(res from step 2) + 1 = 2 (wrong, because expect a = 3 because currently a = 2)
- => Should query the a again to update

---

### Repeatable Read

Other transactions access and update same data like `Read Committed`. But it only see the same data through all the transaction from `beginning` until `commit`

- In the Repeatable Read isolation level, other transactions can read and update the same data concurrently. The key characteristic of Repeatable Read is that within a single transaction, the values of the data that have been read will remain constant, even if other transactions commit changes to that data.
- Breakdowns:
  - **Reads:** Transactions can read data that has been committed by other transactions.
  - **Updates:** Transactions can update data, and those updates become visible to other transactions only after they are committed.
  - **Consistency:** Once a transaction reads a piece of data, it will see the same value for that data throughout the entire transaction, even if other transactions commit changes to that data concurrently.
- It only lock on selected rows, so that if other connection INSERT data, then we selected again -> it causes phantom reads

---

- let a = 1
- Transaction 1: update a -> 2 (not commit yet)
- Transaction 2: read a -> 1 (only read committed data)
- Transaction 1: commit -> a = 2
- (Case 1) Transaction 2: read a **again** -> a = 1
- => Repeatable Read
- (Case 2) Transaction 2: increment a = a + 1 = 1 + 1 = 2 (wrong, because currently a = 2)
- => In this case, event read a again, still leading to not expect result (**caveat**)

---

### Serializable

Transactions are executed sequentially

- let a = 1
- Transaction 1: update a -> 2 (not commit yet)
- Transaction 2: read a -> 1 (prevent by transaction 1)
- Transaction 1: commit -> a = 2
- Transaction 2: read a -> 2

## Isolation levels vs read phenomena

|                  | Dirty read | Non-repeatable read | Phantom read | Default in |
| ---------------- | ---------- | ------------------- | ------------ | ---------- |
| Serializable     | no         | no                  | no           |            |
| Repeatable read  | no         | no                  | yes          |            |
| Read committed   | no         | yes                 | yes          | postgres   |
| Read uncommitted | yes        | yes                 | yes          |            |
