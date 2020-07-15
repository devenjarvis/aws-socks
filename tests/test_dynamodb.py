import socks
import pytest
from unittest.mock import patch

@pytest.fixture()
def mock_boto3():
    with patch('socks.boto3') as mock_boto3:
        mock_boto3.resource().Table().put_item.return_value = {'key': 'value'}
        mock_boto3.resource().Table().update_item.return_value = {'key': 'value'}
        mock_boto3.resource().Table().delete_item.return_value = {'key': 'value'}
        yield mock_boto3

def test_add_item(mock_boto3):
    response = socks.dynamodb.add_item('table', {'key': 'value'}, session=mock_boto3)
    mock_boto3.resource.assert_called_with('dynamodb', region_name='us-east-1')
    mock_boto3.resource().Table.assert_called_with('table')
    mock_boto3.resource().Table().put_item.assert_called_with(Item={'key': 'value'})

def test_update_item(mock_boto3):
    response = socks.dynamodb.update_item('table', {'primary_key': 'value'}, {'some_key': 'some_value'}, session=mock_boto3)
    mock_boto3.resource.assert_called_with('dynamodb', region_name='us-east-1')
    mock_boto3.resource().Table.assert_called_with('table')
    mock_boto3.resource().Table().update_item.assert_called_with(
            Key={'primary_key': 'value'},
            UpdateExpression="SET some_key = :some_key",
            ExpressionAttributeValues={':some_key': 'some_value'}
            )

def test_get_item(mock_boto3):
    response = socks.dynamodb.get_item('table', {'key': 'value'}, session=mock_boto3)
    mock_boto3.resource.assert_called_with('dynamodb', region_name='us-east-1')
    mock_boto3.resource().Table.assert_called_with('table')
    mock_boto3.resource().Table().get_item.assert_called_with(Key={'key': 'value'})

def test_delete_item(mock_boto3):
    response = socks.dynamodb.delete_item('table', {'key': 'value'}, session=mock_boto3)
    mock_boto3.resource.assert_called_with('dynamodb', region_name='us-east-1')
    mock_boto3.resource().Table.assert_called_with('table')
    mock_boto3.resource().Table().delete_item.assert_called_with(Key={'key': 'value'})

def test_scan_table(mock_boto3):
    response = socks.dynamodb.scan_table('table', session=mock_boto3)
    mock_boto3.resource.assert_called_with('dynamodb', region_name='us-east-1')
    mock_boto3.resource().Table.assert_called_with('table')
    mock_boto3.resource().Table().scan.assert_called_with()      