import os
import json
import boto3
from botocore.exceptions import ClientError

dynamo = boto3.resource('dynamodb')
table = dynamo.Table(os.environ['TABLE_NAME'])

def response(code, res):
    return {
        'statusCode': code,
        'body': json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

def put_item(table, item):
    try:
        response = table.put_item(Item=item)
    except ClientError as e:
        return response(500, e.response['Error']['Message'])
    else:
        item = response
        return response(200, item)

def post(event, context):
    item = {
        'id': 1,
        'name': 'book1',
    }
    return put_item(table, item)
