---
title: "To write sargable queries"
---
- Avoid using functions or calculations on indexes columns in WHERE cluase
- Use direct comparision when possible, instead of wrapping the column in a function
  - Example: Using Post.date >= '2023-01-01' instead of YEAR(post) = 2023
- If we need to use **function on a column**, consider creating a **computed column** or
  a function-based index, if the database system supports

- SQL execution orders:
  - FROM
  - JOIN
  - WHERE
  - GROUP BY
  - HAVING
  - SELECT
  - ORDER BY
  - LIMIT
