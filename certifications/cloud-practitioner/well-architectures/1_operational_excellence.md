# Pillar 1: Operational Excellence

- Run and monitor systemwces to **deliver business value** and **continually improve suppoting processes and procdures**
- Design Principles:
  - Perform operations as code - IaaS
  - Annotate documentation: Automate the creation of annotated documentation after every build
  - Make frequent, small, reversible changes: So that in case of any failure, you can reverse it
  - Refine operations procedures frequently
  - Anticipate failure
  - Learn form all operation failures

Example:

1. Prepare
   - CloudFormation, Config
2. Operate
   - CloudFormation, Config, CloudTrail, CloudWatch, X-Ray
3. Evolve
   - CloudFormation, CodeBuild, CodeCommit, CodeDeploy, CodePipeline
