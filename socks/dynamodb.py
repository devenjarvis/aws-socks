import boto3
import json
import decimal
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

#TODO: Write a unit test
def add_item(table_name, item, session=boto3, region_name='us-east-1', **dynamo_table_put_item_kwargs):
    dynamodb_resource = session.resource('dynamodb', region_name=region_name)
    table = dynamodb_resource.Table(table_name)

    #Set kwargs
    dynamo_table_put_item_kwargs['Item'] = item

    try:
        response = table.put_item(**dynamo_table_put_item_kwargs)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        return json.dumps(response, cls=DecimalEncoder)

#TODO: Add error handling
#TODO: Write a unit test
def update_item(table_name, key, item, session=boto3, region_name='us-east-1', **dynamo_table_update_item_kwargs):
    dynamodb_resource = session.resource('dynamodb', region_name=region_name)
    table = dynamodb_resource.Table(table_name)

    #Build ExpressionAttributeValues and UpdateExpression
    expression_attribute_values = {}
    update_expression = "SET "
    for item_key, item_value in item.items():
        expression_attribute_values[f":{item_key}"] = item_value
        update_expression += f"{item_key} = :{item_key}, "
        
    #Clean up trailing comma
    update_expression = update_expression[:-2]

    #Set kwargs
    dynamo_table_update_item_kwargs['Key'] = key
    dynamo_table_update_item_kwargs['UpdateExpression'] = update_expression
    dynamo_table_update_item_kwargs['ExpressionAttributeValues'] = expression_attribute_values

    try:
        response = table.update_item(**dynamo_table_update_item_kwargs)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        return json.dumps(response, cls=DecimalEncoder)

#TODO: Add error handling
#TODO: Write a unit test
def get_item(table_name, key, session=boto3, region_name='us-east-1', **dynamo_table_get_item_kwargs):
    dynamodb_resource = session.resource('dynamodb', region_name=region_name)
    table = dynamodb_resource.Table(table_name)

    #Set kwargs
    dynamo_table_get_item_kwargs['Key'] = key

    try:
        response = table.get_item(**dynamo_table_get_item_kwargs)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        return response['Item']

#TODO: Write a unit test
def delete_item(table_name, key, session=boto3, region_name='us-east-1', **dynamo_table_delete_item_kwargs):
    dynamodb_resource = session.resource('dynamodb', region_name=region_name)
    table = dynamodb_resource.Table(table_name)

    #Set kwargs
    dynamo_table_delete_item_kwargs['Key'] = key

    try:
        response = table.delete_item(**dynamo_table_delete_item_kwargs)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        return json.dumps(response, cls=DecimalEncoder)

#TODO: Expand list of supported operators. Not really ready for use.
#TODO: Add error handling
#TODO: Write a unit test
def query_table(table_name, key_condition_expression, session=boto3, region_name='us-east-1', **dynamo_table_query_kwargs):
    dynamodb_resource = session.resource('dynamodb', region_name=region_name)
    table = dynamodb_resource.Table(table_name)

    #Set kwargs
    dynamo_table_query_kwargs['KeyConditionExpression'] = key_condition_expression

    response = table.query(**dynamo_table_query_kwargs)

    results = []
    for i in response['Items']:
        results.append(json.dumps(i, cls=DecimalEncoder))

    return results

def scan_table(table_name, session=boto3, region_name='us-east-1', **dynamo_table_scan_kwargs):
        dynamodb = session.resource('dynamodb', region_name = region_name)
        table = dynamodb.Table(table_name)

        response = table.scan(**dynamo_table_scan_kwargs)

        results = []
        for i in response['Items']:
            results.append(json.dumps(i, cls=DecimalEncoder))

        # Continue scanning if there are more records
        while 'LastEvaluatedKey' in response:
            response = table.scan()
            for i in response['Items']:
                results.append(json.dumps(i, cls=DecimalEncoder))

        return results 
