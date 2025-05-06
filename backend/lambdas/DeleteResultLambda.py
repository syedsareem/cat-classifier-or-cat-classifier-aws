"""
Lambda function to handle DELETE requests from API Gateway.
Deletes an image classification result from DynamoDB based on the image_key.
"""

import boto3
import json

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CatClassifierTable')

def lambda_handler(event, context):
    try:
        # Extract 'image_key' from query string parameters
        image_key = event['queryStringParameters']['image_key']
        
        # Delete the item with the matching 'image_key'
        table.delete_item(
            Key={
                'image_key': image_key
            }
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'DELETE',
                'Access-Control-Allow-Headers': 'Content-Type',
            },
            'body': json.dumps({'message': f'Image {image_key} deleted successfully.'})
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'DELETE',
                'Access-Control-Allow-Headers': 'Content-Type',
            },
            'body': json.dumps({'error': str(e)})
        }
