import socks
import pytest, json
from unittest.mock import patch

@pytest.fixture()
def mock_boto3():
    with patch('socks.boto3') as mock_boto3:
        yield mock_boto3

def test_invoke_lambda_function(mock_boto3):

    response = socks.aws_lambda.invoke_lambda_function('function_name', pay_load= None, session=mock_boto3, region_name='us-east-1')
    mock_boto3.client.assert_called_with('lambda', region_name='us-east-1')
    invoke_lambda_kwargs = {
        "FunctionName":'function_name',
        "InvocationType": "Event"
        }
    
        
    mock_boto3.client().invoke.assert_called_with(**invoke_lambda_kwargs)