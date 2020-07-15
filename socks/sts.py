import boto3
from botocore.exceptions import ClientError

def assume_role(arn, session=boto3, region_name='us-east-1', **sts_client_assume_role_kwargs):
    sts_client = session.client('sts', region_name=region_name)

    #Set kwargs
    sts_client_assume_role_kwargs['RoleArn'] = arn
    sts_client_assume_role_kwargs['RoleSessionName'] = 'socks_sts_assume_role'

    try:
        response = sts_client.assume_role(**sts_client_assume_role_kwargs)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        session = boto3.Session(
                aws_access_key_id=response['Credentials']['AccessKeyId'],
                aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                aws_session_token=response['Credentials']['SessionToken'])
        return session