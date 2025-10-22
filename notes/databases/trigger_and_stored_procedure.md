---
title: "Trigger and Stored Procedure"
description: "Differences between triggers and stored procedures: event-driven vs on-demand execution and usage scope"
tags:
  - database
  - triggers
  - stored-procedures
  - sql
  - database-design
---
## Usage Scope

Triggers:
- Automatically executed in response to specific events (like INSERT, UPDATE, or DELETE) on a table or view.
- Used to enforce business rules, data integrity, or audit changes without user intervention.

- Specific to a table or view and respond to data changes.
- Used for tasks like logging, auditing, validation, or enforcing referential integrity.

Stored Procedures:
- Manually executed by a user, application, or another procedure.
- Typically used for repetitive tasks such as data processing, calculations, and business logic implementation.

- More general-purpose and can operate across multiple tables or even databases.
- Commonly used for modularizing and reusing complex logic, handling large-scale data processing, or performing administrative tasks.

## Event-Driven vs. On-Demand

Triggers:
 - Event-driven: Activated by events such as INSERT, UPDATE, or DELETE.
 - Cannot be called directly by the user or application.

Stored Procedures:
 - On-demand: Run only when explicitly called or scheduled.
 - Can be invoked multiple times and may accept parameters to alter execution.

