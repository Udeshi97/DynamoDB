import boto3
import json
from decimal import Decimal
# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='cricketplayers',
    KeySchema=[
        {
            'AttributeName': 'fullname',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'year',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'fullname',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)

#put data
item1 = table.put_item(
   Item={
        'fullname': 'Arjuna Ranathunga',
        'year': 1990,
        'testRuns': 5105,
        'ODIRuns': 7456,
        'testRunsAvg': str(Decimal(54.89)),
        'ODIRunsAvg': str(Decimal(27.72)),
        'testWinPercentage': str(Decimal(21.42)),
        'ODIWinPercentage': str(Decimal(46.11)),
    }
)
print(item1)

item2 = table.put_item(
    Item={
        'fullname': 'aravinda de silva',
        'year': 1991,
        'testRuns': 6361,
        'ODIRuns': 6361,
        'testRunsAvg': str(Decimal(68.40)),
        'ODIRunsAvg': str(Decimal(30.14)),
        'testWinPercentage': str(Decimal(0)),
        'ODIWinPercentage': str(Decimal(30.14)),
        }
    )
print(item2)

item3 = table.put_item(
    Item={
        'fullname': 'sanath jayasuriya',
        'year': 1999,
        'testRuns': 6973,
        'ODIRuns': 13430,
        'testRunsAvg': str(Decimal(63.39)),
        'ODIRunsAvg': str(Decimal(30.18)),
        'testWinPercentage': str(Decimal(47.36)),
        'ODIWinPercentage': str(Decimal(55.56)),
        }
    )
print(item3)

item4 = table.put_item(
    Item={
        'fullname': 'mavan athapaththu',
        'year': 2002,
        'testRuns': 5502,
        'ODIRuns': 8529,
        'testRunsAvg': str(Decimal(61.13)),
        'ODIRunsAvg': str(Decimal(31.82)),
        'testWinPercentage': str(Decimal(44.36)),
        'ODIWinPercentage': str(Decimal(55.56)),
        }
    )
print(item4)

item5 = table.put_item(
    Item={
        'fullname': 'mahela jayawardena',
        'year': 2005,
        'testRuns': 11814,
        'ODIRuns': 12650,
        'testRunsAvg': str(Decimal(79.29)),
        'ODIRunsAvg': str(Decimal(28.24)),
        'testWinPercentage': str(Decimal(47.36)),
        'ODIWinPercentage': str(Decimal(53.97)),
        }
    )
print(item5)

item6 = table.put_item(
    Item={
        'fullname': 'kumar sangakkara',
        'year': 2009,
        'testRuns': 12400,
        'ODIRuns': 14234,
        'testRunsAvg': str(Decimal(92.54)),
        'ODIRunsAvg': str(Decimal(35.23)),
        'testWinPercentage': str(Decimal(33.33)),
        'ODIWinPercentage': str(Decimal(60)),
        }
    )
print(item6)

item7 = table.put_item(
    Item={
        'fullname': 'thilakarathne dilshan',
        'year': 2011,
        'testRuns': 5492,
        'ODIRuns': 10290,
        'testRunsAvg': str(Decimal(63.13)),
        'ODIRunsAvg': str(Decimal(31.18)),
        'testWinPercentage': str(Decimal(9.09)),
        'ODIWinPercentage': str(Decimal(42.31)),
        }
    )
print(item7)

item8 = table.put_item(
    Item={
        'fullname': 'angelo mathews',
        'year': 2012,
        'testRuns': 6953,
        'ODIRuns': 5835,
        'testRunsAvg': str(Decimal(69.53)),
        'ODIRunsAvg': str(Decimal(26.77)),
        'testWinPercentage': str(Decimal(38.23)),
        'ODIWinPercentage': str(Decimal(47.12)),
        }
    )
print(item8)

item9 = table.put_item(
    Item={
        'fullname': 'dinesh chandimal',
        'year': 2017,
        'testRuns': 4936,
        'ODIRuns': 3854,
        'testRunsAvg': str(Decimal(70.51)),
        'ODIRunsAvg': str(Decimal(24.55)),
        'testWinPercentage': str(Decimal(21.05)),
        'ODIWinPercentage': str(Decimal(50)),
        }
    )
print(item9)

item10 = table.put_item(
    Item={
        'fullname': 'dimuth karunarathne',
        'year': 2018,
        'testRuns': 6023,
        'ODIRuns': 767,
        'testRunsAvg': str(Decimal(73.45)),
        'ODIRunsAvg': str(Decimal(22.56)),
        'testWinPercentage': str(Decimal(41.66)),
        'ODIWinPercentage': str(Decimal(62.5)),
        }
    )
print(item10)

item11= table.put_item(
    Item={
        'fullname': 'roshan mahanama',
        'year': 1994,
        'testRuns': 2676,
        'ODIRuns': 5162,
        'testRunsAvg': str(Decimal(49.54)),
        'ODIRunsAvg': str(Decimal(24.23)),
        'testWinPercentage': str(Decimal(0)),
        'ODIWinPercentage': str(Decimal(0)),
        }
    )
print(item11)

item12 = table.put_item(
    Item={
        'fullname': 'chaminda vaas',
        'year': 2006,
        'testRuns': 355,
        'ODIRuns': 11014,
        'testRunsAvg': str(Decimal(3.20)),
        'ODIRunsAvg': str(Decimal(34.20)),
        'testWinPercentage': str(Decimal(0)),
        'ODIWinPercentage': str(Decimal(0)),
        }
    )
print(item12)

item13 = table.put_item(
    Item={
        'fullname': 'lahiru thirimanne',
        'year': 2015,
        'testRuns': 2088,
        'ODIRuns': 3194,
        'testRunsAvg': str(Decimal(47.45)),
        'ODIRunsAvg': str(Decimal(25.15)),
        'testWinPercentage': str(Decimal(0)),
        'ODIWinPercentage': str(Decimal(20)),
        }
    )
print(item13)

item14 = table.put_item(
    Item={
        'fullname': 'upul tharanga',
        'year': 2016,
        'testRuns': 1754,
        'ODIRuns': 6951,
        'testRunsAvg': str(Decimal(56.58)),
        'ODIRunsAvg': str(Decimal(29.58)),
        'testWinPercentage': str(Decimal(0)),
        'ODIWinPercentage': str(Decimal(19.05)),
        }
    )
print(item14)

item15 = table.put_item(
    Item={
        'fullname': 'chamara kapugedara',
        'year': 2017,
        'testRuns': 418,
        'ODIRuns': 1624,
        'testRunsAvg': str(Decimal(52.25)),
        'ODIRunsAvg': str(Decimal(15.92)),
        'testWinPercentage': str(Decimal(0)),
        'ODIWinPercentage': str(Decimal(0)),
        }
    )
print(item15)

item16 = table.put_item(
    Item={
        'fullname': 'lasith malinga',
        'year': 2017,
        'testRuns': 3349,
        'ODIRuns': 9760,
        'testRunsAvg': str(Decimal(111.63)),
        'ODIRunsAvg': str(Decimal(43.19)),
        'testWinPercentage': str(Decimal(0)),
        'ODIWinPercentage': str(Decimal(0)),
        }
    )
print(item16)

item17 = table.put_item(
    Item={
        'fullname': 'thisara perera',
        'year': 2017,
        'testRuns': 653,
        'ODIRuns': 5740,
        'testRunsAvg': str(Decimal(108.83)),
        'ODIRunsAvg': str(Decimal(34.58)),
        'testWinPercentage': str(Decimal(0)),
        'ODIWinPercentage': str(Decimal(33.33)),
        }
    )
print(item17)

item18 = table.put_item(
    Item={
        'fullname': 'kusal perera',
        'year': 2021,
        'testRuns': 1177,
        'ODIRuns': 3071,
        'testRunsAvg': str(Decimal(53.50)),
        'ODIRunsAvg': str(Decimal(28.70)),
        'testWinPercentage': str(Decimal(0)),
        'ODIWinPercentage': str(Decimal(33.3)),
        }
    )
print(item18)

item19 = table.put_item(
    Item={
        'fullname': 'dasun shanaka',
        'year': 2021,
        'testRuns': 140,
        'ODIRuns': 1054,
        'testRunsAvg': str(Decimal(23.33)),
        'ODIRunsAvg': str(Decimal(22.91)),
        'testWinPercentage': str(Decimal(0)),
        'ODIWinPercentage': str(Decimal(50)),
        }
    )
print(item19)

#retrieve data

import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
DynamoDBtable = dynamodb.Table('cricketplayers')
response = DynamoDBtable.query(
    KeyConditionExpression=Key('fullname').eq('dasun shanaka') # Input key to query
)

print(response)

#retrieve all data
import boto3
import json

dynamodb = boto3.resource('dynamodb')

DynamoDBtable = dynamodb.Table('cricketplayers')

allUsers = DynamoDBtable.scan()
print(allUsers)

#delete data
import boto3

dynamodb = boto3.resource('dynamodb', region_name= "ap-northeast-1")
DynamoDBtable = dynamodb.Table('cricketplayers') 
# Delete item
response = DynamoDBtable.delete_item(Key = {'fullname': 'dasun shanaka', 'year': 2021}) # Item Key

print(response)

#insert batch
import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')

DynamoDBtable = dynamodb.Table('cricketplayers') # Input table name

# Write items to table
with DynamoDBtable.batch_writer() as batch:
    batch.put_item(Item={"fullname": "dasun shanaka", "year": 2021})
print(batch)

print(response)

#check all
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name= "ap-northeast-1")
DynamoDbtable = dynamodb.Table('cricketplayers')

response = DynamoDBtable.scan()

print("The scan returned the following items:")
for item in response['Items']:
    print(item)
