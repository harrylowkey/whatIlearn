# Microservice

## Synchronous and Asynchronous Communication

1. Synchronous

- Rest API
- gRPC

2. Asynchronous ~ known for Event Driven, Loose Coupling, Distributed services

- NATS
- Kafka
- RabbitMQ

## Pros and Cons

### 1. Synchronous

#### Pros:

Popular protocols and support
Real-time communication

#### Cons:

Blocking communication (waiting for a response in order to perform the next task)
Autonomy (microservices need to know about each other)
Handling of failures during communication

### 2. Asynchronous

#### Pros:

#### Cons:

## Blogs

- [Synchronous communication with gRPC](https://developers.mews.com/synchronous-communication-with-grpc/)
  - Protobuf file: contract
  - Serialize/deserialize the JSON files on each side: **No**
  - Message sizes: The JSON file above takes 25 bytes to represent “id” and “name” values.
    In comparison, the Protobuf will encode the same data to a message that has only 10 bytes (in this case, ~60% size reduction)

## Discuss with ChatGPT

### (?) When to use grpc over the nats or kafka if it is synchronus?

ChatGPT

- The choice between gRPC and messaging systems like NATS or Kafka depends on various factors, and each has its strengths and use cases. Even if gRPC is synchronous, it offers features and characteristics that might make it a better fit for certain scenarios. Here are some considerations for choosing between gRPC and messaging systems:
- Use gRPC when:

  - Strong Typing and Code Generation:
    gRPC relies on Protocol Buffers (protobuf) for message serialization, providing strong typing and automatic code generation in multiple programming languages.
    This can lead to more maintainable and type-safe code.

  - Direct Service-to-Service Communication:
    If direct, point-to-point communication between services is a primary requirement, gRPC can be a good choice. It allows for efficient, bidirectional communication between services.

  - Performance:
    gRPC is known for its performance, especially in terms of low latency and high throughput. It uses HTTP/2 for transport, allowing for multiplexing multiple requests over a single connection.

  - Compatibility with HTTP/2:
    gRPC leverages HTTP/2, which brings advantages such as header compression, multiplexing, and flow control. This can be beneficial for performance in scenarios where a more efficient transport layer is needed.

  - Tight Integration with Frameworks:
    If you're working within an ecosystem that heavily supports gRPC, such as Kubernetes, or if you're building microservices using frameworks like Istio, gRPC might be a natural fit.

- Use Messaging Systems (NATS, Kafka) when:

  - Asynchronous and Event-Driven Architecture:
    If your system requires an event-driven architecture or if you need asynchronous communication between services, messaging systems like NATS or Kafka are well-suited. They allow for decoupling and scalability.

  - Message Brokering:
    Messaging systems excel at message brokering, allowing multiple services to communicate through a central message bus. This can be beneficial for broadcasting events or handling multiple consumers for a single message.

  - Loose Coupling and Scalability:
    If you value loose coupling between services and want to build a scalable, distributed system, messaging systems provide a way for services to communicate without direct dependencies.

  - Durable Message Storage:
    Kafka, in particular, offers durable message storage, making it suitable for scenarios where it's crucial to retain and replay messages for fault tolerance or analytics.

  - Complex Event Processing:
    For scenarios involving complex event processing, pattern matching, or scenarios where events need to be processed by multiple subscribers, messaging systems can be a better fit.

In summary, while gRPC is synchronous, it excels in scenarios that require direct service-to-service communication, strong typing, and high performance. Messaging systems are better suited for asynchronous communication, loose coupling, and event-driven architectures. The choice depends on the specific requirements and characteristics of your microservices architecture. In some cases, a combination of both gRPC and messaging systems might be used in different parts of the system.

### (?) If we use the nats but with request-response pattern, does it the same like using rest API?

ChatGPT

If you use NATS with a request-response pattern, it might resemble the request-response nature of REST APIs, but there are still some key differences between the two approaches.

1.  Synchronous vs. Asynchronous:

    In a traditional request-response over HTTP (REST API), the communication is synchronous. The client sends a request, and it expects an immediate response.
    With NATS in request-response pattern, although it might look similar, the communication is still asynchronous. The client sends a request, but the response is delivered later when the service processes the request.

2.  Decoupling and Loose Coupling:

    NATS with request-response can provide some level of decoupling and loose coupling between services, similar to REST APIs.
    However, messaging systems like NATS generally offer more decoupling capabilities because they allow services to operate independently and asynchronously, even in a request-response pattern.

3.  Scalability:

    NATS can be designed for scalability, just like REST APIs. However, the nature of asynchronous messaging often provides more inherent scalability advantages, as services can process requests independently without waiting for immediate responses.

4.  Fault Tolerance:

    Both NATS with request-response and REST APIs require considerations for fault tolerance. Messaging systems like NATS may have built-in features for retrying messages, which can enhance fault tolerance.

5.  Event-Driven Nature:

    NATS is inherently designed for event-driven architectures, and using it in a request-response pattern may not fully leverage its strengths. Event-driven patterns are often more suitable for messaging systems.

6.  Tooling and Standards:

    REST APIs come with established standards and tooling (like OpenAPI) that can make it easier to document, test, and consume APIs.
    While NATS can be powerful, it may not have the same level of standardized tooling for API documentation and testing.

In summary, while NATS with a request-response pattern might resemble synchronous communication like REST APIs, the underlying nature of messaging systems introduces some differences, particularly in terms of asynchronicity, scalability, and support for event-driven architectures. The choice between NATS and REST API will depend on your specific requirements and the characteristics of your microservices architecture.
