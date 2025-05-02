# DynamoDB Schema — CatClassifierTable

## Table Name
`CatClassifierTable`

## Primary Key
- `image_key` (String) — the S3 object key of the uploaded image

## Attributes
- `catified_result` (String) — the humorous classification
- `original_labels` (String) — top Rekognition label
- `timestamp` (ISO DateTime) — upload time

This table is updated by Lambda after Rekognition processes the image.
