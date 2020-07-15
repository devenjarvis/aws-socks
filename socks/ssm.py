import boto3
import time
from botocore.exceptions import ClientError

class Env():
    def __init__(self, env, session=boto3, region_name='us-east-1'):
        self.env = env
        self.region_name = region_name
        self.session = session

    def get_parameter(self, name, encrypted=False, **ssm_client_get_parameter_kwargs):
        parameter_name = '{}_{}'.format(self.env, name)
        return get_parameter(parameter_name, encrypted, self.session, self.region_name, **ssm_client_get_parameter_kwargs)

def env(env, session=boto3, region_name='us-east-1'):
    return Env(env, session, region_name)

def get_parameter(parameter_name, encrypted=False, session=boto3, region_name='us-east-1', **ssm_client_get_parameter_kwargs):
    ssm_client = session.client('ssm', region_name=region_name)

    #Set kwargs
    ssm_client_get_parameter_kwargs['Name'] = parameter_name
    ssm_client_get_parameter_kwargs['WithDecryption'] = encrypted
    
    while True:
        try:
            parameter = ssm_client.get_parameter(**ssm_client_get_parameter_kwargs)
        except ClientError as e:
            error_code = e.response['Error']['Code']

            if error_code in ['ProvisionedThroughputExceededException', 'ThrottlingException']:
                time.sleep(2)
            else:
                print(f"ERROR: {error_code}")
                raise e
        else:
            return parameter['Parameter']['Value']

        