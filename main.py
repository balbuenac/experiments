import boto3 as boto3
from boto3.dynamodb.conditions import Key

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id='AKIAVP5XHNVLYZSP67MF',
    aws_secret_access_key='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'
)

for bucket in s3.buckets.all():
    print(bucket.name)

# s3.Bucket('saopaulobucket666').upload_file(Filename='demo.txt', Key='demo.txt')

dynamodb = boto3.resource(
        'dynamodb',
        region_name='sa-east-1',
        aws_access_key_id='AKIAVP5XHNVLYZSP67MF',
        aws_secret_access_key='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'
)

table = dynamodb.Table('PropertiesConfig')
response = table.put_item(
   Item={
        'name': 'ruanb',
        'description': 'ruan',
        'last_name': 'bekker',
        'age': 30,
        'account_type': 'administrator',
    }
)

response = table.query(
    KeyConditionExpression=Key('name').eq('ruanb')
)
print(response)
print(response['Items'])
print(response['Items'][0]['last_name'])


