import boto3
from botocore.exceptions import ClientError

class Env():
    def __init__(self, env, session=boto3, region_name='us-east-1'):
        self.env = env
        self.region_name = region_name
        self.session = session

    def get_secret(self, name, **secrets_client_get_secret_value_kwargs):
        secret_name = '{}_{}'.format(self.env, name)
        return get_secret(secret_name, self.session, self.region_name, **secrets_client_get_secret_value_kwargs)

#TODO: Write a unit test
def env(env, session=boto3, region_name='us-east-1'):
    return Env(env, session, region_name)

#TODO: Write a unit test
def get_secret(secret_name, session=boto3, region_name='us-east-1', **secrets_client_get_secret_value_kwargs):
    secrets_client = session.client('secretsmanager', region_name=region_name)

    #Set kwargs
    secrets_client_get_secret_value_kwargs['SecretId'] = secret_name

    try:
        response = secrets_client.get_secret_value(**secrets_client_get_secret_value_kwargs)
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret " + secret_name + " was not found")
    else:
        if 'SecretString' in response:
            return response['SecretString']
        else:
            return response['SecretBinary']