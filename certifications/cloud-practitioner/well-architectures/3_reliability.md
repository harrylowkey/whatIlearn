# Pillar 3: Reliability

- Recover from infra or service disruptions dynamically acuire computing resources to meet demand and
  mitigate disruption such as misconfigurations or transient network issues
- Design Principles:
  - Test recovery procedures: Use automation to simulate different failures or to recreate senerios that led to failures before
  - Automatically recover from failure: Anticipate and remediate failures before they occur
  - Scale horizontally to increase aggreate system availability: Distribute requests across multiple, smaller resources
    to ensure that they don't share common point of failure
  - Stop guessing capacity: Maintain the optimal level to satisfy demand without over or under provisioning -> Use Auto Scaling
