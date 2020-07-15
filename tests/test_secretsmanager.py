import socks
import pytest
from unittest.mock import patch

@pytest.fixture()
def mock_boto3():
    with patch('socks.boto3') as mock_boto3:
        mock_boto3.client().get_secret_value.return_value = {'SecretString': 'this_is_a_secret'}
        yield mock_boto3

def test_parameters_get_single(mock_boto3):
    secretsmanager = socks.secretsmanager.env('env', session=mock_boto3)
    secret = secretsmanager.get_secret('secret_name')
    mock_boto3.client.assert_called_with('secretsmanager', region_name='us-east-1')
    mock_boto3.client().get_secret_value(SecretId='env_secret_name')
    assert secret == 'this_is_a_secret'