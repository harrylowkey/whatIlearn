# Execution Plan

## Components

1. Operators: These symbols illustrate the specific actions taken on the data, delivering tasks such as joining tables or calculating expressions
2. Nodes (or Steps): Found primarily in graphical plans, nodes symbolically represent the operations carried out by operators
The color of a node can indicate its status: white nodes are computed, whereas blue nodes are not. This visual cue helps identify which parts of the query are being executed.
3. Data Flow Arrows: These arrows show how data moves between operators. The thickness of an arrow signifies the volume of rows moving from one operation to the next

## Operators

- Table Scan
- Index Scan
- Index Seek: better than Index Scan (?)
- Key Lookup
- Sort: is one of the most expensive operation
- Spool: Very bad -> it stores data in temporary DB - space issue
- Joins:
    - merge joins: fastest
    - nested joins
    - hash matched joins: significantly slower

## Bad statistics

- Table Scan -> Cluster Index
- Index Scan < Index Seek
- Rid Lookup = Always bad, make sure add Clustered Index

## How to optimize

- Table Scans: Reduce the frequency of table scans by adding appropriate indexes.
- Sorting Operations: Leverage pre-sorted data or modify queries to minimize sorting.
- Hash Matches: Consider alternatives like nested loops if suitable for a more resource-efficient approach.

## Best Practices for Enhancing Query Efficiency

1. Keep Your Queries Simple: Complex joins and nested operations can complicate the optimizer’s task of creating an efficient execution plan. Aiming for simplicity can make SQL Server’s job easier.
2. Use Appropriate Data Types: Ensuring table columns and variables utilize the most suitable data types reduces the necessity for costly casting or conversion operations during query execution.
3. Incorporate Indexing Wisely: Indexes are potent tools for decreasing data retrieval times. Strategic use of Indexing can balance performance improvements against resource demands.
4. Stay Updated with Statistics: SQL Server uses statistics for query planning. Up-to-date statistics lead to improved execution plans.
