from boto3.dynamodb.conditions import Key

import socks
import pytest
from unittest.mock import patch

DYNAMO_QUERY_RESULTS = [
    # First Query
    {
        'Items': [
            {
                'key': 'value'
            },
            {
                'key': 'value'
            }
        ],
        'LastEvaluatedKey': '123'
    },
    # Second Query
    {
        'Items': [
            {
                'key': 'value'
            },
        ]
    }
]

@pytest.fixture()
def mock_boto3():
    with patch('socks.boto3') as mock_boto3:
        mock_boto3.resource().Table().put_item.return_value = {'key': 'value'}
        mock_boto3.resource().Table().update_item.return_value = {'key': 'value'}
        mock_boto3.resource().Table().delete_item.return_value = {'key': 'value'}
        mock_boto3.resource().Table().query.side_effect = [response for response in DYNAMO_QUERY_RESULTS]
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

def test_query_table_with_last_evaluated_key_returned(mock_boto3):
    results = socks.dynamodb.query_table('table', session=mock_boto3, key_condition_expression=Key('key').eq('value'))

    mock_boto3.resource.assert_called_with('dynamodb', region_name='us-east-1')
    mock_boto3.resource().Table.assert_called_with('table')
    assert mock_boto3.resource().Table().query.call_count == len(DYNAMO_QUERY_RESULTS)
    assert len(results) == sum(len(response['Items']) for response in DYNAMO_QUERY_RESULTS)
