"""
Lambda function triggered by S3 PutObject events.
Classifies uploaded images using AWS Rekognition and saves the "catified" label to DynamoDB.
Sends classification results via SNS notification.
"""

import json
import boto3
from datetime import datetime

# AWS clients
rekognition = boto3.client('rekognition')
sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CatClassifierTable')  # Replace if your table name differs

# SNS topic ARN for notifications
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:799480807888:MyCatClassifierNotification"

# Catified label translation dictionary
translation_map = {
    "Dog": "Cat that barks",
    "Pizza": "Flat edible cat",
    "Car": "Fast metal cat",
    "Bird": "Flying cat",
    "Shark": "Water cat with teeth",
    "Bat": "Night flying cat",
    "Person": "Big cat with opinions",
    "Laptop": "Cat that holds the internet",
    "Phone": "Tiny rectangle cat",
    "Chair": "Cat resting structure",
    "Table": "Flat cat staging platform",
    "Bottle": "Cat hydration device",
    "Book": "Silent flat cat",
    "Tree": "Tall natural cat perch",
    "Airplane": "Sky cat",
    "Train": "Long land cat",
    "Bus": "Large people-carrying cat",
    "Cup": "Cat liquid trap",
    "Fridge": "Cold snack cat vault",
    "Bed": "Soft cat recharge zone",
    "Mirror": "Cat echo panel",
    "TV": "Cat movie screen",
    "Keyboard": "Cat piano",
    "Glasses": "Eye helper cat gear",
    "Cat": "Just… a cat. Finally. 🐱"
}

def lambda_handler(event, context):
    # Extract S3 bucket and image key
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Run image analysis using Rekognition
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        MaxLabels=1,
        MinConfidence=75
    )

    # Extract the top label
    labels = response['Labels']
    top_label = labels[0]
    label_name = top_label['Name']

    # Translate the label into a humorous "catified" version
    if label_name in translation_map:
        catified_label = translation_map[label_name]
    else:
        catified_label = f"It's a {label_name}, but still a cat species—just undiscovered."

    # Create a classification message
    result_text = f"Image '{key}' was classified as: {catified_label}"
    print(result_text)

    # Store the classification in DynamoDB
    table.put_item(
        Item={
            'image_key': key,
            'timestamp': datetime.utcnow().isoformat(),
            'original_labels': label_name,
            'catified_result': catified_label
        }
    )

    # Notify users via SNS
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=result_text,
        Subject="📸 Cat Classifier Result"
    )

    return {
        'statusCode': 200,
        'body': json.dumps(result_text)
    }
