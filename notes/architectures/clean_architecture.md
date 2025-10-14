# Clean Architecture

|------------------------|
|    Infrastructure      |  <-- DB, external APIs, frameworks
|------------------------|
|  Interface Adapters    |  <-- Controllers, Presenters, Serializers
|------------------------|
|   Application Layer    |  <-- Use Cases, Application Services
|------------------------|
|      Domain Layer      |  <-- <-- This is where DDD lives
|  (Entities, Aggregates,|
|   Value Objects, etc.) |
--------------------------


[ API (Web Layer) ]    - API Layer: Controllers, filters, DI setup
    ↓
[ Application Layer ]    - Application Layer: Use Cases, Interfaces (Ports), DTOs, Validators
    ↓
[ Domain Layer ]         - Domain Layer: Business rules (Entities, Value Objects, Domain Services)
    ↓
[ Infrastructure Layer ] - Infrastructure Layer: External stuff (EF Core, FileSystem, APIs)








