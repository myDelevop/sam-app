import json
import boto3
import os 

print('Loading Function')

# create the client outside the handler 
dynamo = boto3.client('dynamodb')
region_name = os.environ['REGION_NAME']
table_name = os.environ['TABLE_NAME']


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json'
        },
    }


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    scan_result = dynamo.scan(TableName=table_name)
    return respond(None, res=scan_result)
    #raise Exception("Somethin Wrong")