# Cat Classifier™

A serverless, event-driven AWS project that classifies any image into a humorous cat-themed label — no matter what it actually is.

**Demo link**: https://prod.d3hjaxlit16ap7.amplifyapp.com/

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
2. Receive a humorous catified label
3. Log in via Cognito to delete any result securely

## Postman Collection (API Testing)

This repository includes a Postman collection for testing key API routes.

Available Routes:
Method	Endpoint	Description	Auth Required
GET	/results?image={name}	Fetch classification result	No
GET	/all-results	View all past classifications	No
DELETE	/delete-results	Delete a specific image res	Yes (Cognito)


Using the Collection:
	•	Download and import the JSON file into Postman.
	•	For DELETE requests, use your id_token from Cognito login as a Bearer Token under the Authorization tab.
	•	Replace {name} with the uploaded image file name.

   ## Author

Built by Syed Sareem to demonstrate cloud architecture, serverless workflows, and technical BA depth.
