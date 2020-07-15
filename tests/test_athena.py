import socks
import pytest
from unittest.mock import patch

@pytest.fixture()
def mock_boto3():
    with patch('socks.boto3') as mock_boto3:
        mock_boto3.client().start_query_execution.return_value = {'QueryExecutionId': 'id_123'}
        mock_boto3.client().get_query_execution.return_value = {'QueryExecution': {'Status': {'State': 'SUCCEEDED'}}}
        mock_boto3.resource().Object().load.return_value = {}
        yield mock_boto3

### Test an athena query
def test_athena_query(mock_boto3):    
    data = socks.athena.query("SELECT column FROM table", 'database', 'bucket', 'path', './test.csv', session=mock_boto3)

    mock_boto3.client.assert_called_with('athena', region_name='us-east-1')
    mock_boto3.client().start_query_execution.assert_called_with(QueryString= "SELECT column FROM table",
        QueryExecutionContext= {
            'Database': 'database'
        },
        ResultConfiguration= {
            'OutputLocation': "s3://bucket/path"
    })
    mock_boto3.client().get_query_execution.assert_called_with(QueryExecutionId='id_123')
    mock_boto3.resource.assert_called_with('s3', region_name='us-east-1')
    mock_boto3.resource().Object.assert_called_with('bucket', 'path/id_123.csv')
    mock_boto3.resource().Object().load.assert_called()
    