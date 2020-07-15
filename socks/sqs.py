import boto3
from botocore.exceptions import ClientError
import json

#TODO: Look into other parameters we may want to offer the user
#TODO: Write a unit test
def send_message(message, queue_url, session=boto3, region_name='us-east-1', **sqs_client_send_message_kwargs):
    sqs_client = session.client('sqs', region_name=region_name)
    
    #Convert json/dict to string for the user
    if isinstance(message, dict):
        message = json.dumps(message)

    #Set kwargs
    sqs_client_send_message_kwargs['QueueUrl'] = queue_url
    sqs_client_send_message_kwargs['MessageBody'] = message

    try:
        response = sqs_client.send_message(**sqs_client_send_message_kwargs)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        return response

#TODO: Look into other parameters we may want to offer the user
#TODO: Write a unit test
def receive_message(queue_url, max_num_messages, session=boto3, region_name='us-east-1', **sqs_client_receive_message_kwargs):
    sqs_client = session.client('sqs', region_name=region_name)

    #Set kwargs
    sqs_client_receive_message_kwargs['QueueUrl'] = queue_url
    sqs_client_receive_message_kwargs['MaxNumberOfMessages'] = max_num_messages

    try:
        response = sqs_client.receive_message(**sqs_client_receive_message_kwargs)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        message = response['Messages'][0]
        receipt_handle = response['ReceiptHandle']

        return message, receipt_handle

#TODO: Write a unit test
def delete_message(queue_url, receipt_handle, session=boto3, region_name='us-east-1', **sqs_client_delete_message_kwargs):
    sqs_client = session.client('sqs', region_name=region_name)

    #Set kwargs
    sqs_client_delete_message_kwargs['QueueUrl'] = queue_url
    sqs_client_delete_message_kwargs['ReceiptHandle'] = receipt_handle

    try:
        response = sqs_client.delete_message(**sqs_client_delete_message_kwargs)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        return response