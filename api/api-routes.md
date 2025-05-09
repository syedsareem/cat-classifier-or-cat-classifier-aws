# API Gateway Routes (HTTP API)

## `/results`
- Method: `GET`
- Auth: Public
- Description: Fetch result from DynamoDB using query param `image=<key>`

## `/all-results`
- Method: `GET`
- Auth: Public
- Description: Return all records (used for admin/debug)

## `/delete-result`
- Method: `DELETE`
- Auth: Cognito JWT required
- Description: Delete a classification record by `image_key`

## `/{proxy+}`
- Method: `ANY`
- Auth: Cognito JWT required
- Description: Catch-all route, currently wired to delete

- ## `/define-label`
- Method: `POST`
- Auth: Public
- Description: Accepts a user-defined label when the system encounters an unknown Rekognition result. Saves it to the UserDefinedLables DynamoDB table

