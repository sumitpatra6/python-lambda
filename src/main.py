import os
import json
import logging
import boto3

logger = logging.getLogger()

dynamodb = boto3.resource('dynamodb')

def save_item(item):
    print("Saving items")
    print(item)
    table = dynamodb.Table('TestTable')
    table.put_item(Item=json.loads(item))

def get_all_items():
    print("Querying dynamo db")
    table = dynamodb.Table('TestTable')
    return table.scan().get('Items', [])

def main(event, context):
    try:
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
    except Exception as exp:
        return {
            'statusCode': 500,
            'body': str(exp)
        }