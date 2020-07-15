import socks
import pytest
from unittest.mock import patch
from freezegun import freeze_time

@pytest.fixture()
def mock_boto3():
    with patch('socks.boto3') as mock_boto3:
        mock_boto3.client().describe_log_streams.return_value = {'logStreams':[{'uploadSequenceToken': 'mocked_token', 'logStreamName': 'mocked_stream'}]}
        yield mock_boto3

def test_get_sequence_token(mock_boto3):
    token = socks.cloudwatch.get_sequence_token('mocked_group', 'mocked_stream', session=mock_boto3)
    mock_boto3.client.assert_called_with('logs', region_name='us-east-1')
    mock_boto3.client().describe_log_streams.assert_called_with(logGroupName='mocked_group', logStreamNamePrefix='mocked_stream')
    assert token == 'mocked_token'

@freeze_time("2019-06-01", tz_offset=-4)
def test_push_json_log(mock_boto3):
    response = socks.cloudwatch.push_json_log({'some_key': 'some_value'}, 'mocked_group', 'mocked_stream', session=mock_boto3)
    mock_boto3.client.assert_called_with('logs', region_name='us-east-1')