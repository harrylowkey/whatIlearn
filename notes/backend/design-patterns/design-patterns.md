---
title: "Design patterns"
---
## Creational patterns

### 1. Factory method

#### Definition

The Factory Method Pattern is a creational design pattern.
It provides an interface for creating **products** in a superclass but allows subclasses to alter the type of **products** that will be created.
In essence, it defines an interface for creating **products**, but the specific subclasses decide which concrete class to instantiate.

#### How to Implement

- Creator class
- Factory method inside the creator class that returns an instance of the product
- Products follow the same interface
- Application code with decide which product to create based on subclasses

1. Make all products follow the same **interface**. This interface should declare methods that make sense in every product.

2. Add an empty **factory method** inside the **creator class**. The return type of the method should match the common product interface.

3. In the creator’s code find all references to product constructors. One by one, replace them with calls to the factory method, while extracting the product creation code into the factory method.
You might need to add a temporary parameter to the factory method to control the type of returned product.
At this point, the code of the factory method may look pretty ugly. It may have a large switch statement that picks which product class to instantiate. But don’t worry, we’ll fix it soon enough.

4. Now, create a set of creator subclasses for each type of product listed in the factory method. Override the factory method in the subclasses and extract the appropriate bits of construction code from the base method.

5. If there are too many product types and it doesn’t make sense to create subclasses for all of them, you can reuse the control parameter from the base class in subclasses.
For instance, imagine that you have the following hierarchy of classes: the base Mail class with a couple of subclasses: AirMail and GroundMail ; the Transport classes are Plane ,
Truck and Train . While the AirMail class only uses Plane objects, GroundMail may work with both Truck and Train objects. You can create a new subclass (say TrainMail ) to han- dle both cases, but there’s another option. The client code can pass an argument to the factory method of the GroundMail class to control which product it wants to receive.

6. If, after all of the extractions, the base factory method has become empty, you can make it abstract. If there’s something left, you can make it a default behavior of the method.

#### Example

```java
// The creator class declares the factory method that must
// return an object of a product class. The creator's subclasses
// usually provide the implementation of this method.
class Dialog is
    // The creator may also provide some default implementation
    // of the factory method.
    abstract method createButton(): Button

    // Note that, despite its name, the creator's primary
    // responsibility isn't creating products. It usually
    // contains some core business logic that relies on product
    // objects returned by the factory method. Subclasses can
    // indirectly change that business logic by overriding the
    // factory method and returning a different type of product
    // from it.
    method render() is
        // Call the factory method to create a product object.
        Button okButton = createButton()
        // Now use the product.
        okButton.onClick(closeDialog)
        okButton.render()

// Concrete creators override the factory method to change the
// resulting product's type.
class WindowsDialog extends Dialog is
    method createButton(): Button is
        return new WindowsButton()

class WebDialog extends Dialog is
    method createButton(): Button is
        return new HTMLButton()

// The product interface declares the operations that all
// concrete products must implement.
interface Button is
    method render()
    method onClick(f)

// Concrete products provide various implementations of the
// product interface.
class WindowsButton implements Button is
    method render(a, b) is
        // Render a button in Windows style.
    method onClick(f) is
        // Bind a native OS click event.

class HTMLButton implements Button is
    method render(a, b) is
        // Return an HTML representation of a button.
    method onClick(f) is
        // Bind a web browser click event.

class Application is 
    field dialog: Dialog

    // The application picks a creator's type depending on the 
    // current configuration or environment settings.
    method initialize() is
        config = readApplicationConfigFile()
        if (config.OS == "Windows") then 
            dialog = new WindowsDialog()
        else if (config.OS == "Web") then 
            dialog = new WebDialog()
        else
            throw new Exception("Error! Unknown operating system.")

    // The client code works with an instance of a concrete
    // creator, albeit through its base interface. As long as
    // the client keeps working with the creator via the base
    // interface, you can pass it any creator's subclass.
    method main() is 
        this.initialize() 
        dialog.render()
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
