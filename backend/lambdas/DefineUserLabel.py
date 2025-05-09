import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserDefinedLables')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        original = body.get('OriginalLabel')
        user_label = body.get('UserDefinedLabel')

        if not original or not user_label:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Missing OriginalLabel or UserDefinedLabel"})
            }

        table.put_item(Item={
            'OriginalLabel': original,
            'UserDefinedLabel': user_label,
            'Timestamp': int(datetime.utcnow().timestamp())
        })

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Label saved successfully!"})
        }

    except Exception as e:
        print(f"Error saving user-defined label: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"})
        }
