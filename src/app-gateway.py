import json

print('Loading Function')

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps,
        'headers': {
            'Content-Type': 'application/json'
        },
    }


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    respond(None, res="hello world!")
    #raise Exception("Somethin Wrong")