---
title: "Interview Preparation"
---
## Design patterns

1. Creational design patterns

- Singleton
- Factory Method
- Abstract Factory
- Builder
- Prototype

2. Structural design patterns

- Decorator
- Adapter: Allows incompatible interfaces to work together by converting one interface into another that a client expects.
- Facade: Provides a simplified interface to a complex subsystem, making it easier to use.

- Proxy
- Bridge
- Composite
- Flyweight

3. Behavioral design patterns
- Observer
- Mediator

## Database transaction

**ACID** is a set of properties that ensure reliable processing of database transactions, making them a cornerstone of database management systems. Here's what ACID stands for:

1. **Atomicity**:  
   - Ensures that a transaction is treated as a single, indivisible unit of work. Either all operations within the transaction are completed successfully, or none of them are applied.  
   - Example: In a bank transfer, either both the debit and credit operations occur, or neither does.

2. **Consistency**:  
   - Ensures that a transaction brings the database from one valid state to another, maintaining all defined rules, constraints, and relationships.  
   - Example: After a transfer, the total balance across all accounts remains unchanged.

3. **Isolation**:  
   - Ensures that transactions are executed independently of one another, preventing interference. The results of a transaction are invisible to other transactions until the transaction is complete.  
   - Example: Two users editing the same record won't see partial updates from each other.

4. **Durability**:  
   - Ensures that once a transaction is committed, its changes are permanent, even in the event of a system crash.  
   - Example: After a successful bank transfer, the changes are saved to disk, so the money isn’t lost even if the system fails.

These properties are critical for ensuring data integrity and reliability in database systems, especially in multi-user or distributed environments.

## OOP 4 Pillers
The four pillars of Object-Oriented Programming (OOP) are:

1. **Encapsulation**: 
   - This principle is about bundling the data (attributes) and methods (functions) that operate on the data into a single unit called a class. It also involves restricting access to some of the object's components to prevent unintended interference and misuse. This is usually done by using access modifiers like `private`, `protected`, and `public`.

2. **Abstraction**: 
   - Abstraction involves hiding the complex implementation details of a system and exposing only the necessary functionality to the user. It allows focusing on high-level functionalities while ignoring low-level details. In OOP, abstraction is typically achieved through abstract classes or interfaces.

3. **Inheritance**: 
   - Inheritance allows one class (the child or subclass) to inherit the attributes and methods from another class (the parent or superclass). This promotes code reuse and establishes a relationship between the parent and child classes. A child class can also override or extend the functionality of the parent class.

4. **Polymorphism**: 
   - Polymorphism means "many shapes" and allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different types. The two main types of polymorphism in OOP are:
     - **Compile-time (Static) Polymorphism**: Achieved through method overloading or operator overloading.
     - **Runtime (Dynamic) Polymorphism**: Achieved through method overriding, where a subclass can provide a specific implementation of a method defined in a superclass.

These pillars work together to make OOP a powerful and flexible paradigm for designing and building software systems.

## SOLID Principles

### **S - Single Responsibility Principle (SRP):**
- **Definition**: A class should have only one reason to change, meaning it should only have one responsibility.
- **Explanation**: Each class should focus on a single task or functionality to avoid coupling different functionalities in the same class.
- **Example**: 
  - Bad: A class `Employee` handles employee data and also manages file storage.
  - Good: Split into `Employee` (handles employee data) and `FileStorage` (handles file storage).

---

### **O - Open/Closed Principle (OCP):**
- **Definition**: Classes should be open for extension but closed for modification.
- **Explanation**: You should be able to add new functionality to a class without modifying its existing code, typically through inheritance or interfaces.
- **Example**: 
  - A `PaymentProcessor` class should allow adding new payment methods (e.g., PayPal, Stripe) without changing the base logic.

---

### **L - Liskov Substitution Principle (LSP):**
- **Definition**: Subtypes should be substitutable for their base types without altering the correctness of the program.
- **Explanation**: A derived class must fully implement the functionality expected of its base class.
- **Example**:
  - If `Bird` has a `fly()` method, a subclass `Penguin` should not break the program if substituted (since penguins can’t fly, `fly()` must handle that appropriately).

---

### **I - Interface Segregation Principle (ISP):**
- **Definition**: A class should not be forced to implement interfaces it does not use.
- **Explanation**: Instead of one large interface, create smaller, specific interfaces tailored to different clients' needs.
- **Example**: 
  - Bad: A `Vehicle` interface with `fly()` forces `Car` to implement it.
  - Good: Split into `Drivable` and `Flyable` interfaces.

---

### **D - Dependency Inversion Principle (DIP):**
- **Definition**: High-level modules should not depend on low-level modules. Both should depend on abstractions.
- **Explanation**: Instead of tightly coupling classes, use abstractions (interfaces) to reduce dependency.
- **Example**: 
  - A `ReportGenerator` should depend on an interface `DataSource`, not directly on a `Database`.

---

**Key Benefits:**
- Enhances maintainability.
- Encourages reusable and scalable code.
- Reduces the risk of bugs when making changes or adding features.
