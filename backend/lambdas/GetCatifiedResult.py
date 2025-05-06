"""
Lambda function triggered by API Gateway (GET /results).
Fetches the classification result (catified label) for a specific image from DynamoDB.
"""

import json
import boto3

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CatClassifierTable')  # Replace with your table name if different

def lambda_handler(event, context):
    print("Lambda triggered. Event received:", event)

    # Extract image key from query string parameters
    image_key = event['queryStringParameters']['image']

    try:
        # Query DynamoDB for the image key
        response = table.get_item(Key={'image_key': image_key})
        
        if 'Item' in response:
            # Retrieve the catified classification result
            result = response['Item']['catified_result']
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'GET',
                    'Access-Control-Allow-Headers': 'Content-Type'
                },
                'body': json.dumps({"catified_result": result})
            }
        else:
            # Handle case where image key is not found in the table
            return {
                'statusCode': 404,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'GET',
                    'Access-Control-Allow-Headers': 'Content-Type'
                },
                'body': json.dumps({"message": "Result not found for this image"})
            }
    
    except Exception as e:
        # Handle unexpected errors
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({"error": str(e)})
        }
