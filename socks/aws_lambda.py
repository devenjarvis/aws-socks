import boto3, json
from botocore.exceptions import ClientError


def invoke_lambda_function(function_name, pay_load = None, session=boto3, region_name='us-east-1', **lambda_client_invoke_kwargs):
    lambda_client = session.client('lambda', region_name=region_name)

    #Set kwargs
    lambda_client_invoke_kwargs['FunctionName'] = function_name
    lambda_client_invoke_kwargs['InvocationType'] = "Event"

    if pay_load:
        lambda_client_invoke_kwargs['Payload'] = json.dumps(pay_load)
    
    try:
        response = lambda_client.invoke(**lambda_client_invoke_kwargs)
    except ClientError as e:  
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e 
    else:
        return response  
