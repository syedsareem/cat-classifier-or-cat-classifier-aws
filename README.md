### Cat Classifier™

A serverless AWS project that proves everything is a cat. Kind of.

Welcome to Cat Classifier™, a cloud-native image classification app built entirely on AWS. It uses real machine learning (via Amazon Rekognition) and serverless architecture (S3, Lambda, API Gateway, Cognito) to process any uploaded image and return a cat-themed interpretation—like calling a dog a “cat that barks.”

This project started as a joke during a casual conversation… but it quickly turned into a deep dive into cloud services, security, event-driven design, and Agile-style documentation. It’s now a complete simulation of how I’d approach a real-world product as a Business Analyst in a tech team.

Demo link: https://prod.d3hjaxlit16ap7.amplifyapp.com/
⸻

### Core Features
1. Upload any image via the frontend
2. Automatic label detection using Rekognition
3. Humorous label mapping via a custom dictionary
4. Email notification or API-based result access
5. Secure routes using Cognito authentication
6. Planned: DynamoDB history, favorites, dashboard, CI/CD

### Why This Exists

I built this to:
1. Learn and apply real AWS concepts
2. Simulate working in an Agile team (SAFe-aligned sprints, features, WSJF prioritization)
3. Showcase my ability to manage a technical product from scratch—as a Business Analyst/Product Owner
4. Have fun while building a portfolio project that actually says something


### System Architecture Overview

Cat Classifier™ employs a serverless, event-driven architecture on AWS:

1. **Frontend (HTML/JS)** – Users upload images via a web interface.
2. **Amazon S3** – Stores uploaded images and triggers events upon new uploads.
3. **AWS Lambda** – Processes the image, invokes Amazon Rekognition for label detection, and applies a custom "catified" label mapping.
4. **Amazon Rekognition** – Analyzes images to identify labels.
5. **Amazon SNS** – Sends classification results via email notifications.
6. **Amazon API Gateway & AWS Cognito** – Secures API endpoints for authenticated access.
7. **Amazon DynamoDB (Planned)** – Will store user upload history and metadata for future features like favorites and dashboards.

*Note: For a visual representation, refer to the architecture diagram in the `docs/architecture.md` file (coming soon).*

---

### AWS Services & Configurations

#### Amazon S3
- **Bucket**: `cat-classifier-uploads`
- **CORS**: Allows cross-origin requests from the frontend.
- **Lifecycle Rules**: Automatically deletes objects after 3 days.
- **Triggers**: Invokes Lambda function on new object creation.

#### AWS Lambda
- **Runtime**: Python 3.12
- **Functionality**:
  - Retrieves uploaded image from S3
  - Calls Rekognition for label detection
  - Applies catified dictionary logic
  - Sends result via SNS or returns through API Gateway

#### Amazon Rekognition
- Detects labels in images
- Uses default confidence thresholds
- Only the top label is used for classification

#### Amazon SNS
- **Topic**: `cat-classifier-result-topic`
- Sends result via email notification (temporary delivery mechanism)

#### API Gateway & Cognito
- **Routes**:
  - `DELETE /result` – Removes stored result (secured)
  - `ANY /{proxy+}` – Fallback + testing endpoint (secured)
- **Auth Flow**: Cognito-hosted UI → returns JWT → used in headers for API calls

#### DynamoDB (Planned)
- **Table**: `CatClassifierTable`
- **Schema**:
  - `UserID` (Partition Key)
  - `ImageID` (Sort Key)
  - `OriginalLabel`
  - `CatifiedLabel`
  - `Timestamp`
  - `IsFavorite` (Boolean)

---

### Security & IAM Roles

#### Lambda Execution Role
- Can:
  - Read from S3
  - Call Rekognition
  - Publish to SNS
  - (Planned) Write to DynamoDB

#### Cognito Authenticated Role
- Can:
  - Call protected API Gateway routes
  - Cannot directly access AWS services

---

### Monitoring & Logging

#### AWS CloudWatch
- **Logs**:
  - Lambda executions
  - Rekognition results
  - API Gateway activity
- **Metrics**:
  - Invocation counts and durations
  - SNS delivery status
  - API Gateway error rates

---

> This documentation is maintained as part of my effort to simulate a real product development workflow—including stakeholder-facing documentation, developer onboarding support, and BA-level traceability.



⸻
