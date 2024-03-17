# Cloud Practioner

## Well Architected Framework General Guiding Principles

- Stop guessing your capacity needs
- Test systems at production scale
- Automate to make archtectural experimentation easier
- Allow for evolutionary architectures
  - Design based on changing requirements
- Drive architectures using data
- Improve through game days
  - Simulate applications for flash sale days

## AWS Cloud Best Practices - Design Principles

- Scalability: vertical & horizontal
- Disposable Resources: servers should be disposable & easily configured
- Automation: Serverless, IaaS, Auto Scaling, ...
- Loose Coupling:
  - Monolith are applications that do more and more over time, become beigger
  - Break it down into smaller, loosely copuled components
  - A change or a failure in one component should not cascade to other components
- Services, not Servers
  - Don't use just EC2
  - Use managed services, databases, serverless, etc!

## Well Architected Framework: 6 Pillars

1. [Operational Excellence](./well-architectures/1_operational_excellence.md)
2. [Security](./well-architectures/2_security.md)
3. [Reliability](./well-architectures/3_reliability.md)
4. [Performance Efficiency](./well-architectures/4_performance_efficciency.md)
5. [Cost Optimization](./well-architectures/5_cost_optimization.md)
6. [Sustainability](./well-architectures/6_sustainability.md)

They are not something to balance, or trade-offs, they're a synergy (sức mạnh tổng hợp)
