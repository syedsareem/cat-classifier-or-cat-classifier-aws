# Amazon S3 Configuration for Cat Classifier™ Project

This document outlines how Amazon S3 is configured in the Cat Classifier™ project for secure, scalable, and cost-effective image storage and processing.

---

## Bucket Details

- **Bucket Name**: `my-catclassifier23234`
- **Region**: `us-east-1`
- **Access Control**: Private (uploads use temporary credentials via Cognito Identity Pool)

---

## Lifecycle Rules

To automate storage class transitions and data cleanup, the following lifecycle policy is configured:

### Lifecycle Policy – Current Version Actions:

| Day | Action                                        |
|-----|-----------------------------------------------|
| 0   | Object is uploaded to S3 (Standard Storage)   |
| 30  | Transition to Standard-Infrequent Access (IA) |
| 60  | Transition to Glacier Deep Archive            |
| 90  | Permanently delete (expire) the object        |

This ensures efficient cost management while retaining data for useful periods.

---

## CORS Configuration

To allow secure cross-origin requests (e.g., from a browser-based front end), the following CORS policy is applied to the bucket:

```json
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET", "PUT", "POST", "DELETE"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": []
  }
]

---

### Event Notifications

The bucket is configured to trigger a Lambda function whenever a new object is uploaded.

## Trigger Details:
1. Event Type: s3:ObjectCreated:Put
2. Trigger Target: CatClassifierFunction (AWS Lambda)

## Notification Workflow:
1.	A new image is uploaded.
2.	The Lambda function runs Amazon Rekognition to classify the image.
3.	A “catified” label is generated and stored in DynamoDB.
4.	The result is emailed via SNS to subscribed users.
