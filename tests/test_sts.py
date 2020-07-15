import socks
import pytest
from unittest.mock import patch

@pytest.fixture()
def mock_boto3():
    with patch('socks.boto3') as mock_boto3:
        yield mock_boto3

def test_assume_role(mock_boto3):
    session = socks.sts.assume_role('arn', session=mock_boto3)
    mock_boto3.client.assert_called_with('sts', region_name='us-east-1')
    mock_boto3.client().assume_role.assert_called_with(RoleArn='arn', RoleSessionName='socks_sts_assume_role')
