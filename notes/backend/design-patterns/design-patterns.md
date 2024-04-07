# Design patterns


## Creational patterns

### 1. Factory method

#### Definition

The Factory Method Pattern is a creational design pattern used in software engineering.
It provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.
In essence, it defines an interface for creating objects, but the specific subclasses decide which concrete class to instantiate.

#### How it works

The Factory Method Pattern is a creational design pattern used in software engineering. It provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. In essence, it defines an interface for creating objects, but the specific subclasses decide which concrete class to instantiate.

Here's how it typically works:

Interface/Abstract Class: Define an interface or an abstract class with a method (the factory method) for creating objects. This method will usually return objects of a specific type defined by the interface.

Concrete Classes: Implement subclasses that inherit from the interface/abstract class. These subclasses will provide their own implementation of the factory method, returning instances of the specific class they represent.

Client: The client code will call the factory method to get instances of objects without knowing the concrete class it's dealing with.

#### Example

```python
from abc import ABC, abstractmethod

# Step 1: Define interface/abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @classmethod
    def create(cls):
        pass

# Step 2: Implement concrete classes
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    @classmethod
    def create(cls):
        return Dog()

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

    @classmethod
    def create(cls):
        return Cat()

# Step 3: Client code
def get_animal_sound(animal_type):
    animal = animal_type.create()
    return animal.make_sound()

# Usage
print(get_animal_sound(Dog))  # Output: Woof!
print(get_animal_sound(Cat))  # Output: Meow!

```
---

## Domain-Drivent Design (DDD)

### Repository pattern

#### Definition

The Repository Pattern is a design pattern commonly used in software development, particularly in applications that follow the principles of Domain-Driven Design (DDD) or have a data access layer.
It is a way to separate the logic that retrieves data from a data source from the business logic in the rest of the application.

#### How it works

Repository Interface: Define an interface that specifies the methods for accessing and manipulating data.
These methods often include CRUD operations (Create, Read, Update, Delete) as well as other query methods specific to the domain.

Concrete Repository Implementations: Implement the repository interface in concrete classes. 
These classes are responsible for interacting with the underlying data source, such as a database, web service, or file system.

Client Code: The client code, typically the business logic or services layer, interacts with the repository through its interface, without needing to know the specific implementation details.

#### Example

```python
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def get(self, id):
        pass
    
    @abstractmethod
    def create(self, item):
        pass
    
    @abstractmethod
    def update(self, item):
        pass
    
    @abstractmethod
    def delete(self, id):
        pass

class InMemoryRepository(Repository):
    def __init__(self):
        self.data = {}

    def get(self, id):
        return self.data.get(id)

    def create(self, item):
        self.data[item.id] = item

    def update(self, item):
        if item.id in self.data:
            self.data[item.id] = item
        else:
            raise ValueError("Item does not exist")

    def delete(self, id):
        if id in self.data:
            del self.data[id]
        else:
            raise ValueError("Item does not exist")

class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Usage
repository = InMemoryRepository()
item1 = Item(1, "Item 1")
repository.create(item1)
retrieved_item = repository.get(1)
print(retrieved_item.name)  # Output: Item 1
```
