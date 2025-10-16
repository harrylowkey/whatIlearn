---
title: "SQL Server and PostgreSQL Cheatsheet"
---
### 1. **Data Types**
| Concept             | SQL Server         | PostgreSQL              |
|---------------------|--------------------|-------------------------|
| Integer             | `INT`, `BIGINT`    | `INTEGER`, `BIGINT`     |
| Boolean             | `BIT`              | `BOOLEAN`               |
| Auto Increment      | `INT IDENTITY(1,1)`| `SERIAL` or `BIGSERIAL` |
| Date and Time       | `DATETIME`, `DATE` | `TIMESTAMP`, `DATE`     |
| String (Fixed)      | `CHAR(n)`          | `CHAR(n)`               |
| String (Variable)   | `VARCHAR(n)`, `NVARCHAR` | `VARCHAR(n)`, `TEXT`|

### 2. **AUTO_INCREMENT (Identity Columns)**
| Operation           | SQL Server                    | PostgreSQL                  |
|---------------------|-------------------------------|-----------------------------|
| Define Identity     | `INT IDENTITY(1,1)`           | `SERIAL`                    |
| Retrieve ID         | `SCOPE_IDENTITY()`            | `RETURNING id`              |

### 3. **String Functions**
| Function                   | SQL Server                    | PostgreSQL                      |
|----------------------------|-------------------------------|---------------------------------|
| Concatenate Strings        | `+`                           | `||`                            |
| Convert to Lowercase       | `LOWER(string)`               | `LOWER(string)`                 |
| Substring                  | `SUBSTRING(string, start, length)` | `SUBSTRING(string FROM start FOR length)` |
| Replace                    | `REPLACE(string, find, replace)` | `REPLACE(string, find, replace)` |
| Trim                       | `LTRIM(RTRIM(string))`        | `TRIM(string)`                  |

### 4. **Limiting Results**
| Operation           | SQL Server                  | PostgreSQL              |
|---------------------|-----------------------------|-------------------------|
| Limit Rows          | `SELECT TOP N * FROM table` | `SELECT * FROM table LIMIT N` |
| Pagination          | `OFFSET` only from SQL Server 2012 (`OFFSET M ROWS FETCH NEXT N ROWS ONLY`) | `LIMIT N OFFSET M` |

### 5. **Date Functions**
| Function                     | SQL Server                    | PostgreSQL                    |
|------------------------------|-------------------------------|-------------------------------|
| Current Date/Time            | `GETDATE()`                   | `NOW()`                       |
| Date Difference (Days)       | `DATEDIFF(day, start, end)`   | `end::date - start::date`     |
| Date Add (Days)              | `DATEADD(day, n, date)`       | `date + interval 'n days'`    |
| Date Truncation              | `DATEPART(year, date)`        | `DATE_TRUNC('year', date)`    |

### 6. **Conditional Statements**
| Concept                | SQL Server                    | PostgreSQL                  |
|------------------------|-------------------------------|-----------------------------|
| Conditional Case       | `CASE WHEN ... THEN ... ELSE ... END` | `CASE WHEN ... THEN ... ELSE ... END` |
| IF Statements (in SQL) | `IF ... BEGIN ... END`        | `CASE WHEN ... THEN ... END`          |

### 7. **String Aggregation**
| Operation            | SQL Server                   | PostgreSQL                    |
|----------------------|------------------------------|-------------------------------|
| Concatenate rows     | `STRING_AGG(column, ', ')` (SQL Server 2017+) | `STRING_AGG(column, ', ')`    |
| Legacy Method        | `FOR XML PATH('')`           | `array_agg(column)` or `string_agg(column, ', ')` |

### 8. **Joins**
| Concept                   | SQL Server                | PostgreSQL                   |
|---------------------------|---------------------------|-------------------------------|
| Basic Join Syntax         | Same syntax               | Same syntax                   |
| Cross Apply               | `CROSS APPLY`             | `LATERAL JOIN`                |

### 9. **Transaction Control**
| Concept                  | SQL Server                   | PostgreSQL                    |
|--------------------------|------------------------------|-------------------------------|
| Begin Transaction        | `BEGIN TRANSACTION`          | `BEGIN`                       |
| Commit                   | `COMMIT`                     | `COMMIT`                      |
| Rollback                 | `ROLLBACK`                   | `ROLLBACK`                    |

### 10. **Window Functions**
| Concept                  | SQL Server                       | PostgreSQL                       |
|--------------------------|----------------------------------|----------------------------------|
| Row Number               | `ROW_NUMBER() OVER (ORDER BY ...)` | `ROW_NUMBER() OVER (ORDER BY ...)` |
| Ranking                  | `RANK()`, `DENSE_RANK()`        | `RANK()`, `DENSE_RANK()`        |
| Aggregation with Filter  | `SUM(column) OVER(PARTITION BY ...)` | `SUM(column) OVER(PARTITION BY ...)` |

### 11. **Indexes**
| Concept              | SQL Server                     | PostgreSQL                      |
|----------------------|--------------------------------|---------------------------------|
| Create Index         | `CREATE INDEX idx_name ON table(column)` | Same syntax                   |
| Include Columns      | `CREATE INDEX idx_name ON table(column) INCLUDE (other_column)` | Not directly supported (use covering indexes) |
| Unique Index         | `CREATE UNIQUE INDEX idx_name ON table(column)` | Same syntax                   |

### 12. **Special Commands**
| Concept                       | SQL Server                       | PostgreSQL                    |
|-------------------------------|----------------------------------|-------------------------------|
| Get Table Definition          | `sp_help table`                 | `\d+ table` (in psql)         |
| Show Databases                | `SELECT name FROM sys.databases`| `\l` (in psql)                |
| Show Tables                   | `SELECT name FROM sys.tables`   | `\dt` (in psql)               |

This cheatsheet should cover most differences you'll encounter while switching between SQL Server and PostgreSQL!
