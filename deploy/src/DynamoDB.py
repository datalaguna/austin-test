import boto3

client = boto3.client('dynamodb')

response = client.create_table(
    AttributeDefinitions=[
        {
          "AttributeName": "AffectedFolder",
          "AttributeType": "S"
        },
        {
          "AttributeName": "sla",
          "AttributeType": "S"
        },
        {
          "AttributeName": "files",
          "AttributeType": "L"
        }
    ],
    TableName='Data',
    KeySchema=[
       {
          "AttributeName": "AffectedDate",
          "AttributeType": "S"
        },
    ],
    GlobalSecondaryIndexes=[
        {
          "IndexName": "AffectedFolder_index",
          "KeyAttributes": {
            "PartitionKey": {
              "AttributeName": "AffectedFolder",
              "AttributeType": "S"
            }
          },
          "Projection": {
            "ProjectionType": "ALL"
          }
        }
    ],
    BillingMode='PROVISIONED',
    ProvisionedThroughput={
        'ReadCapacityUnits': 123,
        'WriteCapacityUnits': 123
    },
    TableClass='STANDARD',
    DeletionProtectionEnabled=True,
    ResourcePolicy='string'
)