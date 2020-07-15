import socks
import pytest
from unittest.mock import patch

@pytest.fixture()
def mock_boto3():
    with patch('socks.boto3') as mock_boto3:
        mock_boto3.client().get_parameter.return_value = {'Parameter': { 'Value': 'this_is_a_parameter'}}
        yield mock_boto3

def test_parameters_get_single(mock_boto3):
    ssm = socks.ssm.env('env', session=mock_boto3)
    parameter = ssm.get_parameter('parameter_name')
    mock_boto3.client.assert_called_with('ssm', region_name='us-east-1')
    mock_boto3.client().get_parameter.assert_called_with(Name='env_parameter_name', WithDecryption=False)
    assert parameter == 'this_is_a_parameter'