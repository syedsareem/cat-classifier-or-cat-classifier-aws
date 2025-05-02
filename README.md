# Cat Classifier™

A serverless, event-driven AWS project that classifies any image into a humorous cat-themed label — no matter what it actually is.

## Features

- Upload images via a public S3 website
- Analyze images using Amazon Rekognition
- Convert Rekognition labels into fun “catified” descriptions
- Send classification results via email (SNS)
- Store results in DynamoDB
- View results via secure API Gateway
- Secure deletion using Cognito authentication + JWT
- Frontend built with plain HTML, deployed to CloudFront

## Tech Stack

- AWS S3 + CloudFront (Hosting)
- Lambda (Serverless logic)
- Rekognition (Image analysis)
- DynamoDB (Storage)
- Cognito (Auth)
- API Gateway (Secure API)
- SNS (Notifications)

## Usage

1. Upload an image via the HTML form
2. Receive a humorous catified label via email
3. Log in via Cognito to delete any result securely

   ## Author

Built by Syed Sareem to demonstrate cloud architecture, serverless workflows, and technical BA depth.
