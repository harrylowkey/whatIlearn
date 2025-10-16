---
title: "Database Normalization"
description: "Database Normalization"
tags:
  - database
  - normalization
---
https://www.studytonight.com/dbms/database-normalization.php


1. First Normal Form also known as 1NF

2. Second Normal Form or 2NF

3. Third Normal Form or 3NF

4. Boyce-Codd Normal Form or BCNF

5. Fourth Normal Form or 4NF

6. Fifth Normal Form or 5NF or PJNF (Project-Join Normal Form)

---

## 1. First Normal Form (1NF)

For a table to be in the First Normal Form, it should follow the following 4 rules:

It should only have single(atomic) valued attributes/columns.

Values stored in a column should be of the same domain.

All the columns in a table should have unique names.

And the order in which data is stored should not matter.

## 2. Second Normal Form (2NF)

For a table to be in the Second Normal Form,

It should be in the First Normal form.

And, it should not have *Partial Dependency*

## 3. Third Normal Form (3NF)

A table is said to be in the Third Normal Form when,

It satisfies the First Normal Form and the Second Normal form.

And, it doesn't have **Transitive Dependency**
