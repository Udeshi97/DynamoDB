import json

def lambda_handler(event, context):
    
    employees_list = [
    {
        'id': '1',
        'first_name': "Udeshi",
        'last_name': "Rajapaksha",
        'email': "udeshi@gmail.com"
    },
    {
        "id": '2',
        "first_name": "Steve",
        "last_name": "Palmer",
        "email": "steve@codingthesmartway.com"
    },
    {
        "id": '3',
        "first_name": "Ann",
        "last_name": "Smith",
        "email": "ann@codingthesmartway.com"
    }

    ]
    
    employee_id = event['queryStringParameters']['id']
    
    response = {}
    response['statusCode'] = 200
    response['headers'] = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,GET'
    }
    
    for employee in employees_list:
        if employee['id'] == employee_id:
            response['body'] = json.dumps(employee)
            return response
    
    response['body'] = json.dumps("Employee Not Found")
    return response  