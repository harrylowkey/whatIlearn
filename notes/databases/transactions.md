---
title: "Transactions"
description: "Isolation levels vs read phenomena"
tags:
  - database
  - transaction
---
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

- In the Repeatable Read isolation level, other transactions can read and update the same data concurrently. The key characteristic of Repeatable Read is that within 
a single transaction, the values of the data that have been read will remain constant, even if other transactions commit changes to that data.
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

```
|                  | Dirty read | Non-repeatable read | Phantom read | Default in |
| ---------------- | ---------- | ------------------- | ------------ | ---------- |
| Serializable     | no         | no                  | no           |            |
| Repeatable read  | no         | no                  | yes          |            |
| Read committed   | no         | yes                 | yes          | postgres   |
| Read uncommitted | yes        | yes                 | yes          |            |
```

---
When You DON'T Need Pessimistic Lock:

  1. Read-Only Operations ✓

  // Just reading data - NO LOCK NEEDED
  async getTabList(projectId: string): Promise<TabEntity[]> {
      return this.tabRepo.find({
          where: { projectId },
          order: { position: 'ASC' }
      });
  }

  // Reading for display - NO LOCK NEEDED
  async getTaskDetails(taskId: string): Promise<TaskEntity> {
      return this.taskRepo.findOne({
          where: { id: taskId },
          relations: ['parent', 'children']
      });
  }

  Why no lock? You're not modifying data, so no risk of conflicts.

  ---
  2. Independent Updates (No Read-Calculate-Write Pattern) ✓

  // Updating a single field based on user input - NO LOCK NEEDED
  async updateTaskName(taskId: string, name: string): Promise<void> {
      await this.taskRepo.update({ id: taskId }, { name });
  }

  // Updating status based on direct user choice - NO LOCK NEEDED
  async updateTaskStatus(taskId: string, statusId: string): Promise<void> {
      await this.taskRepo.update({ id: taskId }, { statusId });
  }

  // Setting a flag - NO LOCK NEEDED
  async markAsCompleted(taskId: string): Promise<void> {
      await this.taskRepo.update({ id: taskId }, {
          completed: true,
          completedAt: new Date()
      });
  }

  Why no lock? The update doesn't depend on reading and calculating from other rows.

  ---
  3. Incrementing Counters (Database-Level Atomic Operations) ✓

  // Using database atomic increment - NO LOCK NEEDED
  async incrementViewCount(taskId: string): Promise<void> {
      await this.taskRepo.increment({ id: taskId }, 'viewCount', 1);
      // SQL: UPDATE tasks SET view_count = view_count + 1 WHERE id = $1
  }

  // Database handles atomicity
  async incrementLikes(postId: string): Promise<void> {
      await this.postRepo.increment({ id: postId }, 'likes', 1);
  }

  Why no lock? The database guarantees atomicity with view_count = view_count + 1.

  ---
  4. Creating New Records (No Dependencies on Existing Data) ✓

  // Creating a task with direct user input - NO LOCK NEEDED
  async createTask(projectId: string, dto: CreateTaskDto): Promise<TaskEntity> {
      return this.taskRepo.save({
          projectId,
          name: dto.name,
          description: dto.description,
          type: dto.type,
          // No position calculation needed
      });
  }

  // Logging an event - NO LOCK NEEDED
  async logUserAction(userId: string, action: string): Promise<void> {
      await this.auditLogRepo.save({
          userId,
          action,
          timestamp: new Date()
      });
  }

  Why no lock? Not reading or calculating from existing data.

  ---
  5. Deleting Records (Simple, Direct Deletes) ✓

  // Direct delete by ID - NO LOCK NEEDED
  async deleteTask(taskId: string): Promise<void> {
      await this.taskRepo.delete({ id: taskId });
  }

  // Bulk delete with simple condition - NO LOCK NEEDED
  async deleteCompletedTasks(projectId: string): Promise<void> {
      await this.taskRepo.delete({
          projectId,
          completed: true
      });
  }

  Why no lock? Not calculating positions or modifying related records.

  ---
  6. Reading for Validation (No Write After) ✓

  // Just checking if exists - NO LOCK NEEDED
  async checkTaskExists(taskId: string): Promise<boolean> {
      return this.taskRepo.exists({ where: { id: taskId } });
  }

  // Validating permissions - NO LOCK NEEDED
  async validateUserCanAccessTask(userId: string, taskId: string): Promise<boolean> {
      const task = await this.taskRepo.findOne({
          where: { id: taskId },
          relations: ['project.members']
      });
      return task?.project.members.some(m => m.userId === userId);
  }

  Why no lock? Just validating, not updating based on the read.

  ---
  When You DO Need Pessimistic Lock:

  Pattern: Read → Calculate → Write (based on what you read)

  This is the key pattern where race conditions occur!

  Example 1: Position Calculation (Your use case)

  // NEEDS LOCK ❌ Without lock
  async reorderPosition(...) {
      // 1. READ: Get current positions
      const tabs = await this.tabRepo.find({ where: { projectId } });

      // 2. CALCULATE: Determine new position based on read data
      const newPosition = (tabs[0].position + tabs[1].position) / 2;

      // 3. WRITE: Update based on calculation
      await this.tabRepo.save({ id: tabId, position: newPosition });
  }

  Race condition: Two transactions read same data, calculate same position!

  // WITH LOCK ✓
  async reorderPosition(...) {
      await this.tabRepo.find({
          where: { projectId },
          lock: { mode: 'pessimistic_write' }  // 🔒
      });

      // Now safe: only one transaction at a time
      const newPosition = this.calculate(...);
      await this.tabRepo.save({ id: tabId, position: newPosition });
  }

  ---
  Example 2: Inventory Management

  // NEEDS LOCK ❌
  async purchaseProduct(productId: string, quantity: number) {
      // 1. READ
      const product = await this.productRepo.findOne({
          where: { id: productId }
      });

      // 2. CALCULATE
      if (product.stock < quantity) {
          throw new Error('Insufficient stock');
      }
      const newStock = product.stock - quantity;

      // 3. WRITE
      await this.productRepo.update({ id: productId }, { stock: newStock });
  }

  Race condition: Both transactions see stock=10, both allow purchase of 10, stock goes negative!

  // WITH LOCK ✓
  async purchaseProduct(productId: string, quantity: number) {
      const product = await this.productRepo.findOne({
          where: { id: productId },
          lock: { mode: 'pessimistic_write' }  // 🔒
      });

      if (product.stock < quantity) {
          throw new Error('Insufficient stock');
      }

      await this.productRepo.update({ id: productId }, {
          stock: product.stock - quantity
      });
  }

  ---
  Example 3: Account Balance Transfer

  // NEEDS LOCK ❌
  async transferMoney(fromAccountId: string, toAccountId: string, amount: number) {
      // 1. READ
      const fromAccount = await this.accountRepo.findOne({
          where: { id: fromAccountId }
      });

      // 2. CALCULATE
      if (fromAccount.balance < amount) {
          throw new Error('Insufficient funds');
      }

      // 3. WRITE
      await this.accountRepo.update({ id: fromAccountId }, {
          balance: fromAccount.balance - amount
      });
      await this.accountRepo.update({ id: toAccountId }, {
          balance: toAccount.balance + amount
      });
  }

  Race condition: Account could be overdrawn by concurrent transfers!

  // WITH LOCK ✓
  async transferMoney(fromAccountId: string, toAccountId: string, amount: number) {
      const fromAccount = await this.accountRepo.findOne({
          where: { id: fromAccountId },
          lock: { mode: 'pessimistic_write' }  // 🔒
      });

      const toAccount = await this.accountRepo.findOne({
          where: { id: toAccountId },
          lock: { mode: 'pessimistic_write' }  // 🔒
      });

      if (fromAccount.balance < amount) {
          throw new Error('Insufficient funds');
      }

      await this.accountRepo.update({ id: fromAccountId }, {
          balance: fromAccount.balance - amount
      });
      await this.accountRepo.update({ id: toAccountId }, {
          balance: toAccount.balance + amount
      });
  }

  ---
  Example 4: Generating Sequential Numbers

  // NEEDS LOCK ❌
  async generateInvoiceNumber(companyId: string) {
      // 1. READ
      const lastInvoice = await this.invoiceRepo.findOne({
          where: { companyId },
          order: { number: 'DESC' }
      });

      // 2. CALCULATE
      const newNumber = (lastInvoice?.number || 0) + 1;

      // 3. WRITE
      return this.invoiceRepo.save({
          companyId,
          number: newNumber
      });
  }

  Race condition: Duplicate invoice numbers!

  // WITH LOCK ✓
  async generateInvoiceNumber(companyId: string) {
      const lastInvoice = await this.invoiceRepo.findOne({
          where: { companyId },
          order: { number: 'DESC' },
          lock: { mode: 'pessimistic_write' }  // 🔒
      });

      const newNumber = (lastInvoice?.number || 0) + 1;

      return this.invoiceRepo.save({
          companyId,
          number: newNumber
      });
  }

  ---
  Quick Decision Tree:

  Do you need to UPDATE data?
  │
  ├─ NO → No lock needed ✓
  │
  └─ YES → Is the update based on READING existing data?
             │
             ├─ NO (direct user input) → No lock needed ✓
             │
             └─ YES → Does the calculation depend on data that
                      could be modified by other transactions?
                      │
                      ├─ NO (single row atomic) → No lock needed ✓
                      │
                      └─ YES → NEED PESSIMISTIC LOCK! 🔒

  ---
  Summary:

  You DON'T need pessimistic lock when:
  - ✅ Read-only operations
  - ✅ Updates with direct user input (not calculated)
  - ✅ Atomic database operations (increment/decrement)
  - ✅ Creating records without dependencies
  - ✅ Simple deletes

  You NEED pessimistic lock when:
  - ❌ Read → Calculate → Write pattern
  - ❌ Position/ordering calculations
  - ❌ Stock/inventory management
  - ❌ Balance transfers
  - ❌ Sequential number generation
  - ❌ Any operation where the WRITE depends on the READ

  Your understanding is spot on! 🎯
