import json
import boto3
from datetime import datetime

# AWS clients
rekognition = boto3.client('rekognition')
sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CatClassifierTable')
user_defined_table = dynamodb.Table('UserDefinedLables')

# Your SNS topic ARN
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:799480807888:MyCatClassifierNotification"

# Catified label translation map
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
    "Cat": "Just… a cat."
}

def get_user_defined_label(original_label):
    try:
        response = user_defined_table.get_item(Key={'OriginalLabel': original_label})
        item = response.get('Item')
        if item and 'UserDefinedLabel' in item:
            print(f"User-defined label found: {item['UserDefinedLabel']}")
            return item['UserDefinedLabel']
    except Exception as e:
        print(f"DynamoDB lookup error: {e}")
    
    return None

def lambda_handler(event, context):
    # Extract image info from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Call Rekognition to analyze image
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        MaxLabels=1,
        MinConfidence=75
    )

    # Get top label
    labels = response['Labels']
    top_label = labels[0]
    label_name = top_label['Name'].strip().lower()

    # Translate label using the catification map or user-defined label
    if label_name = ['cat', 'kitten']:
        catified_label = "It's a cat!"
    elif label_name in translation_map:
        catified_label = translation_map[label_name]
    else:
        user_label = get_user_defined_label(label_name)
        if user_label:
            catified_label = user_label
        else:
            catified_label = f"It's a {label_name}, but still a cat species—just undiscovered."

    # Format result string
    result_text = f"Image '{key}' was classified as: {catified_label}"
    print(result_text)

    # Save result in DynamoDB
    table.put_item(
        Item={
            'image_key': key,
            'timestamp': datetime.utcnow().isoformat(),
            'original_labels': label_name,
            'catified_result': catified_label
        }
    )

    # Send result via SNS
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=result_text,
        Subject="📸 Cat Classifier Result"
    )

    return {
        'statusCode': 200,
        'body': json.dumps(result_text)
    }
