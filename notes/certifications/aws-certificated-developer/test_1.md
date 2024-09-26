# Test 1

1. A developer is defining the signers that can create signed URLs for their Amazon CloudFront distributions.
Which of the following statements should the developer consider while defining the signers? (Select two)

A. When you create a signer, the public key is with CloudFront and private key is used to sign a portion of URL
B. When you use the root user to manage CloudFront key pairs, you can only have up to two active CloudFront key pairs per AWS account


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

- X-Ray:
- VPC Flow Logs:
- CloundTrail:

- CDK deployment: Create the app from a template provided by AWS CDK not by AWS CloudFormation.

- Load Balancer: can target EC2 instances only within an AWS Region.

- ASG:Auto Scaling group can contain EC2 instances in *one or more Availability Zones* within the *same Region* but cannot span across *multiple Regions*.

- CDK:  AWS CDK is a framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation.
The CDK Toolkit again poses regional limitations not for everiy regions

- SAM sections required: Transform, Resources

- EBS volumes: are AZ locked

- KMS Encryption: can encrypt up to 4 kilobytes (4096 bytes) of arbitrary data
- KMS: maximum data size supported by AWS KMS is 4KB


- RDS: Automated backups are limited to a single AWS Region while manual snapshots and Read Replicas are supported across multiple Regions.

- Automated backups: are limited to a single AWS Region

- SSE-KMS encryption mechanism -> 'x-amz-server-side-encryption': 'aws:kms' in header
- SSE-S3 server-side encryption mechanism -> 'x-amz-server-side-encryption': 'AES256' in header



## Questions:

[?] You are running workloads on AWS and have embedded RDS database connection strings within each web server hosting your applications.
After failing a security audit, you are looking at a different approach to store your secrets securely and automatically rotate the database credentials.
Which AWS service can you use to address this use-case?
[A]: Systems Manager

[?] CodeCommit is a managed version control service that hosts private Git repositories in the AWS cloud.
Which of the following credential types is NOT supported by IAM for CodeCommit?
[A]: IAM username and password

[?] Question 9
Incorrect
A developer has an application that stores data in an Amazon S3 bucket. The application uses an HTTP API to store and retrieve objects. When the PutObject API operation adds objects to the S3 bucket the developer must encrypt these objects at rest by using server-side encryption with Amazon S3-managed keys (SSE-S3).
Which solution will guarantee that any upload request without the mandated encryption is not processed?
[A]: Invoke the PutObject API operation and set the x-amz-server-side-encryption header as AES256 (- not ss3:s3).
Use an S3 bucket policy to deny permission to upload an object unless the request has this header

[?] Which of the following security credentials can only be created by the AWS Account root user?
[A]: CloudFront Key pairs

[?] 
As part of his development work, an AWS Certified Developer Associate is creating policies and attaching them to IAM identities.
After creating necessary Identity-based policies, he is now creating Resource-based policies.
Which is the only resource-based policy that the IAM service supports?
[A] Trust policy

[?] Which of the following mechanisms is not supported for API Gateway?
[A]: STS


