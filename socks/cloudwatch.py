import boto3
from botocore.exceptions import ClientError

import datetime
import json
import time

#TODO: Error handling
#TODO: Write a unit test
def get_sequence_token(group_name, stream_name, session=boto3, region_name='us-east-1'):
    cw_client = session.client('logs', region_name=region_name)
    while True:
        try:
            response = cw_client.describe_log_streams(logGroupName=group_name, logStreamNamePrefix=stream_name)
        except ClientError as e:
            error_code = e.response['Error']['Code']

            #Wait and try again if we are being throttled
            if error_code in ['ThrottlingException']:
                print('Cloudwatch describe_log_streams is throttling you. Trying again in 2 seconds.')
                time.sleep(2)
            else:
                print(f"ERROR: {error_code}")
                raise e
        else:
            if response['logStreams'] and response['logStreams'][0]['logStreamName'] == stream_name:
                if('uploadSequenceToken' in response['logStreams'][0]):
                    return response['logStreams'][0]['uploadSequenceToken']
                else:
                    return None
            else:
                cw_client.create_log_stream(logGroupName=group_name, logStreamName=stream_name)
                return None


#TODO: Should this return something?
#TODO: Error handling
#TODO: Write a unit test
def push_json_log(log_body, group_name, stream_name, session=boto3, region_name='us-east-1', **cw_client_put_log_events_kwargs):
    cw_client = session.client('logs', region_name=region_name)
    log_time = datetime.datetime.now();

    #Set kwargs
    cw_client_put_log_events_kwargs['logGroupName'] = group_name
    cw_client_put_log_events_kwargs['logStreamName'] = stream_name
    cw_client_put_log_events_kwargs['logEvents'] = [
        {
            'timestamp': int(log_time.timestamp() * 1000.0),
            'message': json.dumps(log_body)
        }
    ]

    sequence_token = get_sequence_token(group_name, stream_name, session=session, region_name=region_name)
    if sequence_token:
        cw_client_put_log_events_kwargs['sequenceToken'] = sequence_token
    try:
        response = cw_client.put_log_events(**cw_client_put_log_events_kwargs)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        return response