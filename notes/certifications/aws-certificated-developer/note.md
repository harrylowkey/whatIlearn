# Notes

## Services

- Amazon Kinesis Data Streams: 
allows you to continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams,
database event streams, financial transactions, social media feeds, IT logs, and location-tracking events.

- Amazon Kinesis Firehose: 
fully managed service for delivering real-time streaming data to destinations such as Amazon S3, Amazon Redshift,
Amazon OpenSearch Service (formerly Elasticsearch Service), and third-party services like Datadog and Splunk.
It simplifies the process of capturing, transforming, and loading streaming data into these destinations.

- Security Group: stateful
- Network ACL: stateless
- SQS: The queue along with all its contents has to be deleted after testing - *Delete Queue*, not *Remove Queue*

- AWS KMS: Maximum data size supported by AWS KMS is 4KB
- X-Ray:
- VPC Flow Logs:
- CloudTrail:

- CDK deployment: Create the app from a template provided by AWS CDK not by AWS CloudFormation.

- Load Balancer: can target EC2 instances only within an AWS Region.
- ASG: Auto Scaling group can contain EC2 instances in *one or more Availability Zones* within the *same Region* but cannot span across *multiple Regions*.

- CDK: AWS CDK is a framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation.
The CDK Toolkit again poses regional limitations not for everiy regions

- SAM sections required: Transform, Resources

- EBS volumes: are AZ locked

- KMS Encryption: can encrypt up to 4 kilobytes (4096 bytes) of arbitrary data
- KMS: maximum data size supported by AWS KMS is 4KB

- RDS: Automated backups are limited to a single AWS Region while
Manual snapshots and Read Replicas are supported across multiple Regions.

- SSE-KMS encryption mechanism -> 'x-amz-server-side-encryption': 'aws:kms' in header
- SSE-S3 server-side encryption mechanism -> 'x-amz-server-side-encryption': 'AES256' in header
- the x-amz-server-side-encryption header has no such value as sse:s3
-> x-amz-server-side-encryption header goes with AES256

- API Gateway:
 -> work with: Cognito User Pools, Standard AWS IAM roles and policies, Lambda Authorizer
 - not work with: AWS Security Token Service (AWS STS)

- X-Forwarded-For Not X-Forwarded-From
- EBS volumes support both in-flight encryption and encryption at rest using KMS

- Opt for Rolling deployment - This deployment type is present for AWS Elastic Beanstalk and not for EC2 instances directly.
- Opt for Immutable deployment - This deployment type is present for AWS Elastic Beanstalk and not for EC2 instances directly.

- The Lambda function invocation is asynchronous

- Cloudformation
    - command: cloudformation package and cloudformation deploy
    - 'Dependencies' section of the template -> Invalid
    - Which section of a CloudFormation template cannot be associated with Condition?
    -> Paramteers

- Cloudformation: To create a cross-stack reference, use the Export output field to flag the value of a resource output for export.
Then, use the Fn::ImportValue intrinsic function to import the value.

You cannot use the Ref intrinsic function to import the value.

- The application uses STS to request credentials but after an hour your application stops working.
-> Credentials that are created by using account credentials can range from 900 seconds (15 minutes) up to a maximum of 3,600 seconds (1 hour), with a default of 1 hour.
Hence you need to renew the credentials post expiry.

- EBS security features: Region-specific settings, encryption by default

- logs:DescribeLogStreams notlogs:DescribeLogGroup

- SQS maximum maximum number of messages that can be retrieved at one time: 10

-  Amazon RDS:
    - RDS applies OS updates by performing maintenance on the standby, then promoting the standby to primary and 
    finally performing maintenance on the old primary,which becomes the new standby
    - Amazon RDS automatically initiates a failover to the standby, in case primary database fails for any reason 

- Kinesis Data Streams cost > Kinesis Firehose

- Track user activity: Using CloudTrail

## Not to do anything question

- An organization is moving its on-premises resources to the cloud. Source code will be moved to AWS CodeCommit and AWS CodeBuild will be used for compiling the source code
using Apache Maven as a build tool.
The organization wants the build environment should allow for scaling and running builds in parallel.
Which of the following options should the organization choose for their requirement?
-> CodeBuild scales automatically, the organization does not have to do anything for scaling or for parallel builds

- An organization recently began using AWS CodeCommit for its source control service.
A compliance security team visiting the organization was auditing the software development process
and noticed developers making many git push commands within their development machines.
The compliance team requires that encryption be used for this activity.
How can the organization ensure source code is encrypted in transit and at rest?
-> Repositories are automatically encrypted at rest

- A company’s e-commerce website is expecting hundreds of thousands of visitors on Black Friday.
The marketing department is concerned that high volumes of orders might stress SQS leading to message failures.
The company has approached you for the steps to be taken as a precautionary measure against the high volumes.
What step will you suggest as a Developer Associate?
-> Amazon SQS is highly scalable and does not need any intervention to handle the expected high volumes

---
## Questions:

- To enable HTTPS connections for his web application deployed on the AWS Cloud, a developer is in the process of creating server certificate.
Which AWS entities can be used to deploy SSL/TLS server certificates? (Select two)
-> IAM
-> AWS Certificate Manager


- A developer is defining the signers that can create signed URLs for their Amazon CloudFront distributions.
Which of the following statements should the developer consider while defining the signers? (Select two)
A. When you create a signer, the public key is with CloudFront and private key is used to sign a portion of URL
B. When you use the root user to manage CloudFront key pairs, you can only have up to two active CloudFront key pairs per AWS account

[?] You are running workloads on AWS and have embedded RDS database connection strings within each web server hosting your applications.
After failing a security audit, you are looking at a different approach to store your secrets securely and automatically rotate the database credentials.
Which AWS service can you use to address this use-case?
[A]: Systems Manager

[?] CodeCommit is a managed version control service that hosts private Git repositories in the AWS cloud.
Which of the following credential types is **NOT supported** by IAM for CodeCommit?
[A]: IAM username and password

[?] A developer has an application that stores data in an Amazon S3 bucket. The application uses an HTTP API to store and retrieve objects.
When the PutObject API operation adds objects to the S3 bucket the developer must encrypt these objects at rest 
by using server-side encryption with Amazon S3-managed keys (SSE-S3).
Which solution will guarantee that any upload request without the mandated encryption is not processed?
[A]: Invoke the PutObject API operation and set the x-amz-server-side-encryption header as AES256 (- not ss3:s3).
Use an S3 bucket policy to deny permission to upload an object unless the request has this header

[?] Which of the following security credentials can only be created by the AWS Account root user?
[A]: CloudFront Key pairs

[?] As part of his development work, an AWS Certified Developer Associate is creating policies and attaching them to IAM identities.
After creating necessary Identity-based policies, he is now creating Resource-based policies.
Which is the only resource-based policy that the IAM service supports?
[A] Trust policy

[?] Which of the following mechanisms is not supported for API Gateway?
[A]: STS

[?] A Developer at a company is working on a CloudFormation template to set up resources. Resources will be defined using code and 
provisioned based on certain conditions defined in the Conditions section.
Which section of a CloudFormation template cannot be associated with Condition?
[A]: Parameters

- Auto Scaling groups that span across multiple Regions need to be enabled for all the Regions specified - 
-> This is not valid for Auto Scaling groups. Auto Scaling groups *cannot* span across multiple Regions.

- The manager at an IT company wants to set up member access to user-specific folders in an Amazon S3 bucket - bucket-a.
So, user x can only access files in his folder - bucket-a/user/user-x/ and user y can only access files in her folder - bucket-a/user/user-y/ and so on.
As a Developer Associate, which of the following IAM constructs would you recommend so that the policy snippet can be made generic for all team members and 
the manager does not need to create separate IAM policy for each team member?
-> `IAM policy variables` 

- The Technical Lead of your team has reviewed a CloudFormation YAML template written by a new recruit and specified that an invalid section has been added to the template.
Which of the following represents an invalid section of the CloudFormation template?
-> 'Dependencies' section of the template

- How will you invoke the !FindInMap function to fulfill
-> !FindInMap [ MapName, TopLevelKey, SecondLevelKey ]

- Your company has stored all application secrets in SSM Parameter Store. The audit team has requested to get a report to better understand when and 
who has issued API calls against SSM Parameter Store. Which of the following options can be used to produce your report?
-> Use AWS CloudTrail to get a record of actions taken by a user
Not correct: Use SSM Parameter Store Access Logs in CloudWatch Logs to get a record of actions taken by a user - CloudWatch Logs can be integrated but that will not help determine who issued API calls.

- A multi-national company has just moved to AWS Cloud and it has configured forecast-based AWS Budgets alerts for cost management.
However, no alerts have been received even though the account and the budgets have been created almost three weeks ago.
What could be the issue with the AWS Budgets configuration?
-> AWS requires **approximately 5 weeks** of usage data to generate budget forecasts

- A company is using a Border Gateway Protocol (BGP) based AWS VPN connection to connect from its on-premises data center to Amazon EC2 instances in the company’s account.
The development team can access an EC2 instance in subnet A but is unable to access an EC2 instance in subnet B in the same VPC.
Which logs can be used to verify whether the traffic is reaching subnet B?
-> VPC Flow Logs
Not correct: Subnet logs

- As a Team Lead, you are expected to generate a report of the code builds for every week to report internally and to the client.
This report consists of the number of code builds performed for a week, the percentage success and failure, and overall time spent on these builds by the team members.
You also need to retrieve the CodeBuild logs for failed builds and analyze them in Athena.
Which of the following options will help achieve this?
-> Enable S3 and CloudWatch Logs integration

- The technology team at an investment bank uses DynamoDB to facilitate high-frequency trading where multiple trades can try and update an item at the same time.
Which of the following actions would make sure that only the last updated value of any item is used in the application?
-> Use ConsistentRead = true while doing GetItem operation for any item

- A serverless application built on AWS processes customer orders 24/7 using an AWS Lambda function and communicates with an external vendor's HTTP API for payment processing.
The development team wants to notify the support team in near real-time using an existing Amazon Simple Notification Service (Amazon SNS) topic,
but only when the external API error rate exceeds 5% of the total transactions processed in an hour.
As an AWS Certified Developer Associate, which option will you suggest as the most efficient solution?
-> Configure and **push high-resolution** custom metrics to CloudWatch that record the failures of the external payment processing API calls.
Create a CloudWatch alarm that sends a notification via the existing SNS topic when the error rate exceeds the specified rate

---
- As a developer, you are looking at creating a custom configuration for Amazon EC2 instances running in an Auto Scaling group.
The solution should allow the group to auto-scale based on the metric of 'average RAM usage' for your Amazon EC2 instances.
Which option provides the best solution?
-> Create a custom metric in CloudWatch and make your instances send data to it using PutMetricData. Then, create an alarm based on this metric

- The development team at a company wants to encrypt a 111 GB object using AWS KMS.
Which of the following represents the best solution?
-> Make a GenerateDataKey API call that returns a plaintext key and an encrypted copy of a data key. Use a plaintext key to encrypt the data

- A large firm stores its static data assets on Amazon S3 buckets. Each service line of the firm has its own AWS account.
For a business use case, the Finance department needs to give access to their S3 bucket's data to the Human Resources department.
Which of the below options is NOT feasible for cross-account access of S3 bucket objects?
-> Use IAM roles and resource-based policies delegate access across accounts within different partitions via programmatic access only

- A telecom service provider stores its critical customer data on Amazon Simple Storage Service (Amazon S3).
Which of the following options can be used to control access to data stored on Amazon S3? (Select two)
-> Query String Authentication, Access Control Lists (ACLs)
-> Bucket policies, Identity and Access Management (IAM) policies

- Your company has a three-year contract with a healthcare provider.
The contract states that monthly database backups must be retained for the duration of the contract for compliance purposes. 
Currently, the limit on backup retention for automated backups, on Amazon Relational Database Service (RDS), does not meet your requirements.
Which of the following solutions can help you meet your requirements?
-> Create a cron event in CloudWatch, which triggers an AWS Lambda function that triggers the database snapshot

- A development team has created a new IAM user that has s3:putObject permission to write to an S3 bucket. 
This S3 bucket uses server-side encryption with AWS KMS managed keys (SSE-KMS) as the default encryption. 
Using the access key ID and the secret access key of the IAM user, the application received an access denied error when calling the PutObject API.
As a Developer Associate, how would you resolve this issue?
-> Correct the policy of the IAM user to allow the kms:GenerateDataKey action

- A company’s e-commerce website is expecting hundreds of thousands of visitors on Black Friday.
The marketing department is concerned that high volumes of orders might stress SQS leading to message failures.
The company has approached you for the steps to be taken as a precautionary measure against the high volumes.
What step will you suggest as a Developer Associate?
-> Amazon SQS is highly scalable and does not need any intervention to handle the expected high volumes

- You have been asked by your Team Lead to enable detailed monitoring of the Amazon EC2 instances your team uses.
As a Developer working on AWS CLI, which of the below command will you run?
-> aws ec2 monitor-instances **--instance-ids** i-1234567890abcdef0
Not aws ec2 monitor-instances **--instance-id** i-1234567890abcdef0

- A media company uses Amazon Simple Queue Service (SQS) queue to manage their transactions.
With changing business needs, the payload size of the messages is increasing. The Team Lead of the project is worried about the 256 KB message size limit that SQS has.
What can be done to make the queue accept messages of a larger size?
-> Use the SQS Extended Client

- To meet compliance guidelines, a company needs to ensure replication of any data stored in its S3 buckets.
Which of the following characteristics are correct while configuring an S3 bucket for replication?
-> S3 lifecycle actions are not replicated with S3 replication
-> Same-Region Replication (SRR) and Cross-Region Replication (CRR) can be configured at the S3 bucket level, a shared prefix level, or an object level using S3 object tags

- You have a workflow process that pulls code from AWS CodeCommit and deploys to EC2 instances associated with tag group ProdBuilders.
You would like to configure the instances to archive no more than two application revisions to conserve disk space.
Which of the following will allow you to implement this?
-> CodeDeploy Agent

- An organization is moving its on-premises resources to the cloud. Source code will be moved to AWS CodeCommit and AWS CodeBuild will be used for compiling the source code
using Apache Maven as a build tool.
The organization wants the build environment should allow for scaling and running builds in parallel.
Which of the following options should the organization choose for their requirement?
-> CodeBuild scales automatically, the organization does not have to do anything for scaling or for parallel builds

---
- An organization recently began using AWS CodeCommit for its source control service.
A compliance security team visiting the organization was auditing the software development process
and noticed developers making many git push commands within their development machines.
The compliance team requires that encryption be used for this activity.
How can the organization ensure source code is encrypted in transit and at rest?
-> Repositories are automatically encrypted at rest

- A developer is configuring an Application Load Balancer (ALB) to direct traffic to the application's EC2 instancesand Lambda functions.
Which of the following characteristics of the ALB can be identified as correct? (Select two)
-> An ALB has three possible target types: Instance, IP and Lambda
-> You can not specify publicly routable IP addresses to an ALB

- A development team had enabled and configured CloudTrail for all the Amazon S3 buckets used in a project.
The project manager owns all the S3 buckets used in the project. However, the manager noticed that he did not receive
any object-level API access logs when the data was read by another AWS account.
What could be the reason for this behavior/error?
-> The bucket owner also needs to be object owner to get the object access logs

- You are a manager for a tech company that has just hired a team of developers to work on the company's AWS infrastructure.
All the developers are reporting to you that when using the AWS CLI to execute commands it fails with the following exception:
You are not authorized to perform this operation. Encoded authorization failure message: 
6h34GtpmGjJJUm946eDVBfzWQJk6z5GePbbGDs9Z2T8xZj9EZtEduSnTbmrR7pMqpJrVYJCew2m8YBZQf4HRWEtrpncANrZMsnzk.
Which of the following actions will help developers decode the message?
-> AWS STS decode-authorization-message

- A development team is considering Amazon ElastiCache for Redis as its in-memory caching solution for its relational database.
Which of the following options are correct while configuring ElastiCache? (Select two
-> All the nodes in a Redis cluster must reside in the same region
-> While using Redis with cluster mode enabled, you cannot manually promote any of the replica nodes to primary

- As part of internal regulations, you must ensure that all communications to Amazon S3 are encrypted.
For which of the following encryption mechanisms will a request get rejected if the connection is not using HTTPS?
-> SSE-C

- What is the run order of the hooks for in-place deployments using CodeDeploy?
-> Application Stop -> Before Install -> Application Start -> ValidateService 

- You are reviewing scripts for the deployment process located in the AppSpec file.
-> DownloadBundle => BeforeInstall => ApplicationStart => ValidateService

- Your company manages hundreds of EC2 instances running on Linux OS.
The instances are configured in several Availability Zones in the eu-west-3 region.
Your manager has requested to collect system memory metrics on all EC2 instances using a script.
Which of the following solutions will help you collect this data?
-> Use a cron job on the instances that pushes the EC2 RAM statistics as a Custom metric into CloudWatch

- A developer is migrating an on-premises application to AWS Cloud. The application currently processes user uploads and uploads them to a local directory on the server.
All such file uploads must be saved and then made available to all instances in an Auto Scaling group.
As a Developer Associate, which of the following options would you recommend for this use-case?
-> Use Amazon S3 and make code changes in the application so all uploads are put on S3

- An IT company is using AWS CloudFormation to manage its IT infrastructure.
It has created a template to provision a stack with a VPC and a subnet. The output value of this subnet has to be used in another stack.
As a Developer Associate, which of the following options would you suggest to provide this information to another stack?
-> Export/Import

---
- A developer has created a new Application Load Balancer but has not registered any targets with the target groups.
Which of the following errors would be generated by the Load Balancer?
-> HTTP 503: Service unavailable

- You would like your Elastic Beanstalk environment to expose an HTTPS endpoint instead of an HTTP endpoint to get in-flight encryption
between your clients and your web servers. What must be done to set up HTTPS on Beanstalk?
-> Create a config file in the .ebextensions folder to configure the Load Balancer

- Which of the following CLI options will allow you to retrieve a subset of the attributes coming from a DynamoDB scan?
-> --projection-expression
A projection expression is a string that identifies the attributes you want. To retrieve a single attribute, specify its name. For multiple attributes, the names must be comma-separated.
--filter-expression - If you need to further refine the Query results, you can optionally provide a filter expression. A filter expression determines which items within the Query results should be returned to you. All of the other results are discarded. A filter expression is applied after Query finishes, but before the results are returned. Therefore, a Query will consume the same amount of read capacity, regardless of whether a filter expression is present.

- You were assigned to a project that requires the use of the AWS CLI to build a project with AWS CodeBuild.
Your project's root directory includes the buildspec.yml file to run build commands and would like your build artifacts to be automatically encrypted at the end.
How should you configure CodeBuild to accomplish this?
-> Specify a KMS key to use

- Your company wants to move away from manually managing Lambda in the AWS console and wants to upload and update them using AWS CloudFormation.
How do you declare an AWS Lambda function in CloudFormation? (Select two)
-> Upload all the code as a zip to S3 and refer the object in AWS::Lambda::Function block
-> Write the AWS Lambda code inline in CloudFormation in the AWS::Lambda::Function block as long as there are no third-party dependencies

- An IT company leverages CodePipeline to automate its release pipelines. The development team wants to write a Lambda function that will send notifications 
for state changes within the pipeline.
As a Developer Associate, which steps would you suggest to associate the Lambda function with the event source?
-> Set up an Amazon CloudWatch Events rule that uses CodePipeline as an event source with the target as the Lambda function

- An e-commerce application posts its order transactions in bulk to an accounting application for further processing.
Due to changes in the compliance rules, all the transactions are being encrypted with AWS Key Management Service (AWS KMS) key
before posting to the accounting application. Post this change, the testers have raised tickets regarding the application receiving a ThrottlingException error.
What measures should a developer take to fix this issue MOST optimally? (Select two)
-> Use the data key caching feature with the AWS Encryption SDK encryption library
-> Reduce the rate of requests and consider using the backoff and retry logic

- An EC2 instance has an IAM instance role attached to it, providing it read and write access to the S3 bucket 'my_bucket'.
You have tested the IAM instance role and both reads and writes are working. You then remove the IAM role from the EC2 instance and test both read and write again.
Writes stopped working but reads are still working.
What is the likely cause of this behavior?
-> The S3 bucket policy authorizes reads

- You have created a DynamoDB table to support your application and provisioned RCU and WCU to it so that your application has been running for over a year now
without any throttling issues. Your application now requires a second type of query over your table and as such,
you have decided to create an LSI and a GSI on a new table to support that use case. One month after having implemented such indexes,
it seems your table is experiencing throttling.
Upon looking at the table's metrics, it seems the RCU and WCU provisioned are still sufficient. What's happening?
-> The GSI is throttling so you need to provision more RCU and WCU to the GSI
If you perform heavy write activity on the table, but a global secondary index on that table has insufficient write capacity,
then the write activity on the table will be throttled. To avoid potential throttling, the provisioned write capacity for a global secondary index
should be equal or greater than the write capacity of the base table since new updates will write to both the base table and global secondary index.

- X-Ray: Create Index -> Using Annotations

- You are a developer working on AWS Lambda functions that are triggered by Amazon API Gateway and would like 
to perform testing on a low volume of traffic for new API versions. Which of the following features will accomplish this task?
-> Canary Deployment

- AWS SQS FIFO - ordering -> MessageGroupID
Not MessageOrderId

- As part of your video processing application, you are looking to perform a set of repetitive and scheduled tasks asynchronously. Your application is deployed on Elastic Beanstalk.
Which Elastic Beanstalk environment should you set up for performing the repetitive tasks?
-> Setup a Worker environment and a cron.yaml file

- Your Lambda function must use the Node.js drivers to connect to your RDS PostgreSQL database in your VPC.
How do you bundle your Lambda function to add the dependencies?
-> Put the function and the dependencies in one folder and zip them together

- You would like to run the X-Ray daemon for your Docker containers deployed using AWS Fargate.
What do you need to do to ensure the setup will work? (Select two)
-> Deploy the X-Ray daemon agent as a **sidecar** container
-> Provide the correct IAM task role to the X-Ray container

- Which environment variable can be used by AWS X-Ray SDK to ensure that the daemon is correctly discovered on ECS?
-> AWS_XRAY_DAEMON_ADDRESS

- A company has recently launched a new gaming application that the users are adopting rapidly. The company uses RDS MySQL as the database.
The development team wants an urgent solution to this issue where the **rapidly increasing workload might exceed the available database storage**.
As a developer associate, which of the following solutions would you recommend so that it requires minimum development effort to address this requirement?
-> Enable storage auto-scaling for RDS MySQL

- You would like to paginate the results of an S3 List to show 100 results per page to your users and minimize the number of API calls that you will use.
Which CLI options should you use? (Select two)
-> --max-items
-> --starting-token
Not --page-size, --limit

- A financial services company uses Amazon S3 to store transformed and anonymized customer data that is generated by a daily batch job.
The development team has been tasked to build a solution that analyzes the output of the daily job for any sensitive financial information about the company's customers.
As an AWS Certified Developer Associate, which of the following options would you recommend to address this use case MOST efficiently?
-> Leverage Macie to analyze the output of the daily batch job and look for any sensitive data findings of type SensitiveData:S3Object/Financial

---

- A video streaming application uses Amazon CloudFront for its data distribution. The development team has decided to use CloudFront with origin failover for high availability.
Which of the following options are correct while configuring CloudFront with Origin Groups? (Select two)
-> CloudFront fails over to the secondary origin only when the HTTP method of the viewer request is GET, HEAD or OPTIONS
-> CloudFront routes all incoming requests to the primary origin, even when a previous request failed over to the secondary origin

- A development team has been using Amazon S3 service as an object store. With Amazon S3 turning strongly consistent,
the team wants to understand the impact of this change on its data storage practices.
As a developer associate, can you identify the key characteristics of the strongly consistent data model followed by S3? (Select two)
-> If you delete a bucket and immediately list all buckets, the deleted bucket might still appear in the list
Bucket configurations have an eventual consistency model. If you delete a bucket and immediately list all buckets, the deleted bucket might still appear in the list.
-> A process deletes an existing object and immediately tries to read it. Amazon S3 will not return any data as the object has been deleted
Amazon S3 provides strong read-after-write consistency for PUTs and DELETEs of objects in your Amazon S3 bucket in all AWS Regions.
This applies to both writes to new objects as well as PUTs that overwrite existing objects and DELETEs.

- A Company uses a large set of EBS volumes for their fleet of Amazon EC2 instances. As an AWS Certified Developer Associate, your help has been requested to understand 
the security features of the EBS volumes. The company does not want to build or maintain their own encryption key management infrastructure.
Can you help them understand what works for Amazon EBS encryption? (Select two)
-> Encryption by default is a Region-specific setting. If you enable it for a Region, you cannot disable it for individual volumes or snapshots in that Region
-> A volume restored from an encrypted snapshot, or a copy of an encrypted snapshot is always encrypted
=> EBS security features: Region-specific 

- A multi-national company maintains separate AWS accounts for different verticals in their organization. 
The project manager of a team wants to migrate the Elastic Beanstalk environment from Team A's AWS account into Team B's AWS account.
As a Developer, you have been roped in to help him in this process.
Which of the following will you suggest?
-> Create a saved configuration in Team A's account and download it to your local machine. Make the account-specific parameter changes and upload to the S3 bucket 
in Team B's account. From Elastic Beanstalk console, create an application from 'Saved Configurations'

- Your team has just signed up an year-long contract with a client maintaining a three-tier web application, that needs to be moved to AWS Cloud.
The application has steady traffic throughout the day and needs to be on a reliable system with no down-time or access issues.
The solution needs to be cost-optimal for this startup.
Which of the following options should you choose?
-> Amazon EC2 Reserved Instances

Performnace: on-primises > reserved = on-demand > spot
Finance: on-primises > on-demand > reserved  > spot
Sleep: Spot

- A company wants to implement authentication for its new RESTful API service that uses Amazon API Gateway. 
To authenticate the calls, each request must include HTTP headers with a client ID and user ID.
These credentials must be compared to the authentication data in a DynamoDB table.
As an AWS Certified Developer Associate, which of the following would you recommend for implementing this authentication in API Gateway?
-> Develop an AWS Lambda authorizer that references the authentication data in the DynamoDB table
Not choose Amazon Cognito because we want to customize auth in headers
