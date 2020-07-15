import socks
import pytest
from unittest.mock import patch

@pytest.fixture()
def mock_boto3():
    with patch('socks.boto3') as mock_boto3:
        mock_boto3.client().receive_message.return_value = {'Messages': ['some_message'], 'ReceiptHandle': 'receipt_handle'}
        yield mock_boto3

def test_send_message(mock_boto3):
    response = socks.sqs.send_message({'some_key': 'some_value'}, 'url', session=mock_boto3)
    mock_boto3.client.assert_called_with('sqs', region_name='us-east-1')
    mock_boto3.client().send_message.assert_called_with(QueueUrl='url', MessageBody='{"some_key": "some_value"}')

def test_receive_message(mock_boto3):
    message, receipt_handle = socks.sqs.receive_message('url', 1, session=mock_boto3)
    mock_boto3.client.assert_called_with('sqs', region_name='us-east-1')
    mock_boto3.client().receive_message.receive_message(QueueUrl='url', MaxNumberOfMessages=1)
    assert message == 'some_message'
    assert receipt_handle == 'receipt_handle'

def delete_message(mock_boto3):
    response = socks.sqs.send_message('url', 'receipt_handle', session=mock_boto3)
    mock_boto3.client.assert_called_with('sqs', region_name='us-east-1')
    mock_boto3.client().delete_message.assert_called_with(QueueUrl='url', ReceiptHandle='receipt_handle')