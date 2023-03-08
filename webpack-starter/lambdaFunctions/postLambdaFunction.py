import json

def lambda_handler(event, context):
    newEmployee = json.loads(event['body'])
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin':'*',
        },
        'body': json.dumps(newEmployee)
    }
