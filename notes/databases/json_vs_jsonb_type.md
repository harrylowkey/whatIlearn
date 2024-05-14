# JSON vs JSONB in PostgreSQL

<!-- published_date: 13 May, 2024 -->
<!-- description: JSON vs JSONB in PostgreSQL -->
<!-- tags: database -->

Ref: https://www.dbvis.com/thetable/json-vs-jsonb-in-postgresql-a-complete-comparison/

JSON:
 - Does not support indexing

JSONB:
 - Supports indexing: GIN, GIST

JSON > JSONB when:
 - You have to perform a lot of INSERT operations
 - You do not expect to perform complex queries on your JSON data
 - You need to preserve the original JSON data indentation and format

JSONB > JSON when:
 - Storing user tracking data that needs to be updated over time
 - Storing permission or configuration data
 - Storing highly nested data whose structure may change over time

JSON vs. JSONB: Main differences

The main difference between json and jsonb lies in the way they store data behind the scene. This makes jsonb inherently more efficient than json. Specifically, the json data type stores an exact copy of the input text. So, each function and operation has to reparse the entire field at each execution.

At the same time, this can also represent an advantage over jsonb. This is because json preserves the indentation of the input data. So, if you need to be careful about JSON formatting, the json PostgreSQL data type can be useful.

On the other hand, jsonb stores data in a decomposed binary format. This makes the `INSERT` operation a bit slower compared to json due to conversion overhead. However, the jsonb binary format is significantly faster to process because it does not involve reparsing. Also, jsonb supports many more functions and operators than json.

Moreover, jsonb supports indexing. This can lead to significant performance advantages when parsing and querying JSON data.
