# Notes

---

## **Amazon CloudFront**
- **Signers for CloudFront Distributions**:
  - **A**: Public key stored in CloudFront, private key used to sign the URL.
  - **B**: Only the root user can create CloudFront key pairs; a maximum of two active key pairs per AWS account.

---

## **Amazon S3**
- **Encryption**:
  - **SSE-KMS**: `'x-amz-server-side-encryption': 'aws:kms'` (for server-side encryption with KMS-managed keys).
  - **SSE-S3**: `'x-amz-server-side-encryption': 'AES256'` (for server-side encryption with S3-managed keys).

- **Bucket Policy**:
  - **Prevent uploads without encryption**: Use S3 bucket policy to deny uploads unless `'x-amz-server-side-encryption'` header is set to `'AES256'`.

- **IAM Policy for Folder Access**:
  - **IAM Policy Variables**: Used to create generic policies for folder access in S3

- **Replication**:
  - **S3 Lifecycle Actions** are not replicated with S3 replication.
  - Both **Same-Region Replication (SRR)** and **Cross-Region Replication (CRR)** can be configured at different levels using S3 object tags.

- **S3 Access Control**:
  - Use **Query String Authentication** and **Access Control Lists (ACLs)**.
  - Use **Bucket Policies** and **IAM Policies**.

---

## **Amazon RDS**
- **Backups**:
  - **Automated backups**: Limited to a single AWS Region.
  - **Manual snapshots** and **Read Replicas**: Supported across multiple regions.

- **Backup Retention Solution**:
  - Use **CloudWatch** to trigger an **AWS Lambda** function to take manual database snapshots for retention beyond automated backup limits.

---

## **Amazon Kinesis**
- **Data Streams**: Capture gigabytes of data per second from multiple sources.
- **Firehose**: Delivers real-time streaming data to S3, Redshift, and third-party services (e.g., Datadog, Splunk).

---

## **Amazon SQS**
- **Delete Queue** after testing, not just removing the queue.
- **Payload Size**: To handle payloads larger than 256 KB, use **SQS Extended Client**.
- **High-Volume Handling**: SQS scales automatically; no action needed for high traffic.

---

## **AWS API Gateway**
- Works with **Cognito User Pools**, **AWS IAM roles**, and **Lambda Authorizer**.
- **Not supported**: **AWS Security Token Service (AWS STS)**.

---

## **AWS Lambda**
- **Invocation**: Lambda function invocation is asynchronous.

---

## **IAM & Security**
- **Supported IAM Credential Types** for CodeCommit:
  - Not supported: **IAM username and password**.

- **Resource-Based Policies**:
  - The only resource-based policy in IAM is the **Trust Policy**.

---

## **Amazon EC2**
- **Detailed Monitoring**: Use the CLI command:
  ```bash
  aws ec2 monitor-instances --instance-ids <instance-id>
  ```

- **Custom Metrics**:
  - To auto-scale based on **RAM usage**, create a custom metric in CloudWatch and send instance data using `PutMetricData`.

---

## **AWS CloudFormation**
- **Unsupported Section**: **Parameters** section cannot be associated with Conditions.
- **Correct Syntax**: `!FindInMap [MapName, TopLevelKey, SecondLevelKey]`.
- **Invalid Section**: No **Dependencies** section.

---

## **AWS CodeDeploy**
- **Revision Management**: Use **CodeDeploy Agent** to limit revisions (e.g., archive only two application revisions).

---

## **AWS CodeBuild**
- **Automatic Scaling**: CodeBuild automatically scales; no need for manual intervention.
- **Parallel Builds**: CodeBuild supports parallel builds automatically.

---

## **AWS X-Ray and VPC Flow Logs**
- **Troubleshooting Connectivity**:
  - Use **VPC Flow Logs** to verify traffic reaching different subnets.
  
---

## **AWS KMS**
- **Maximum Data Size**: AWS KMS can encrypt up to **4 KB** (4096 bytes) of data.
- **Encrypting Large Data**: Use `GenerateDataKey` API for data larger than 4 KB, encrypt data with the plaintext key, and store the encrypted data key.

---

## **Auto Scaling Group (ASG)**
- Can span across **multiple AZs** but only within the **same Region** (not across Regions).

---

## **AWS Budgets**
- **Forecast Alerts**: Requires approximately **5 weeks** of usage data to generate budget forecasts.

---

## **CloudWatch & SNS**
- **Monitor API Errors**:
  - Push custom high-resolution metrics to CloudWatch and set up alarms to send notifications via SNS when error rates exceed a defined threshold (e.g., 5% error rate for API transactions).

---

## **Miscellaneous**
- **CodeBuild Logs**: Store failed build logs in S3 and analyze using **Athena**.
- **Rotating Database Secrets**: Use **AWS Systems Manager Parameter Store** for securely storing and rotating database credentials.

