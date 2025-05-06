### Lambda Functions Overview

This project uses multiple AWS Lambda functions to handle different parts of the Cat Classifier™ pipeline. Below are the key functions and their responsibilities:

⸻

## 1. CatClassifierFunction
	•	Trigger: S3 PUT event (file upload).
	•	Purpose: Uses Amazon Rekognition to detect labels from the uploaded image, translates them into “catified” labels, stores results in DynamoDB, and sends email via SNS.
	•	Permissions Required:
	•	rekognition:DetectLabels
	•	sns:Publish
	•	dynamodb:PutItem
	•	IAM Role: CatClassifierFunction-role-9v5l34uo with inline policy for DynamoDB access.

⸻

## 2. GetCatifiedResult
	•	Trigger: HTTP GET request via API Gateway (/results?image=filename.jpg).
	•	Purpose: Retrieves the classification result from DynamoDB using the image key.
	•	Permissions Required:
	•	dynamodb:GetItem
	•	Authentication: Public (no Cognito required).

⸻

## 3. GetAllLambdaResults
	•	Trigger: HTTP GET request via API Gateway (/all-results).
	•	Purpose: Scans DynamoDB to return all classification history.
	•	Permissions Required:
	•	dynamodb:Scan
	•	Authentication: Public (no Cognito required).

⸻

## 4. DeleteResultLambda
	•	Trigger: HTTP DELETE request via API Gateway (/delete-results).
	•	Purpose: Deletes a specific result from DynamoDB using the image key.
	•	Permissions Required:
	•	dynamodb:DeleteItem
	•	Authentication: Secured using Cognito JWT authorizer.

⸻
