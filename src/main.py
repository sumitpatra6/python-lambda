import os
import json
import logging
import boto3

logger = logging.getLogger()
if os.getenv('ENV'):
    dynamodb = boto3.resource('dynamodb')

def save_item(item):
    print("Saving items")
    table = dynamodb.Table('TestTable')
    table.put_item(Item=item)

def get_all_items():
    print("Querying dynamo db")
    table = dynamodb.Table('TestTable')
    return table.scan()

def main(event, context):
    print(event)
    method = event.get("httpMethod", "")
    body = event.get("body", {})
    if method == "POST":
        save_item(body)
        return {
        'statusCode': 200,
        'body': json.dumps({
            'message' : "Success"
        })
        
    }

    if method == "GET":
        return {
        'statusCode': 200,
        'body': json.dumps({
            'data' : get_all_items()
        })
    }