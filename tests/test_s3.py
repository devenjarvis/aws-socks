import socks
import pytest
from unittest.mock import patch

@pytest.fixture()
def mock_boto3():
    with patch('socks.boto3') as mock_boto3:
        mock_boto3.resource().Object().get()['Body'].read().decode.return_value = '{"sample_key": "sample_value"}'
        yield mock_boto3

def test_read_file(mock_boto3):
    file = socks.s3.read_file('bucket', 'key.json', session=mock_boto3, PartNumber=123)

    mock_boto3.resource.assert_called_with('s3', region_name='us-east-1')
    mock_boto3.resource().Object.assert_called_with('bucket', 'key.json')
    mock_boto3.resource().Object().get.assert_called_with(PartNumber=123)
    assert 'sample_key' in file
    assert file['sample_key'] == 'sample_value'

def test_download_file(mock_boto3):
    response = socks.s3.download_file('local_path', 'bucket', 'key.json', session=mock_boto3)

    mock_boto3.resource.assert_called_with('s3', region_name='us-east-1')
    mock_boto3.resource().Object.assert_called_with('bucket', 'key.json')
    mock_boto3.resource().Object().download_fileobj.assert_called()

def test_write_file(mock_boto3):
    response = socks.s3.write_file('content', 'bucket', 'key.json', session=mock_boto3)

    mock_boto3.resource.assert_called_with('s3', region_name='us-east-1')
    mock_boto3.resource().Object.assert_called_with('bucket', 'key.json')
    mock_boto3.resource().Object().put.assert_called()

def test_upload_file(mock_boto3):
    response = socks.s3.upload_file('local_path', 'bucket', 'key.json', session=mock_boto3)

    mock_boto3.resource.assert_called_with('s3', region_name='us-east-1')
    mock_boto3.resource().Object.assert_called_with('bucket', 'key.json')
    mock_boto3.resource().Object().upload_file.assert_called_with(Filename='local_path')

def test_delete_file(mock_boto3):
    response = socks.s3.delete_file('bucket', 'key.json', session=mock_boto3)

    mock_boto3.resource.assert_called_with('s3', region_name='us-east-1')
    mock_boto3.resource().Object.assert_called_with('bucket', 'key.json')
    mock_boto3.resource().Object().delete.assert_called_with()

def test_list_files(mock_boto3):
    response = socks.s3.list_files('bucket', 'prefix/', session=mock_boto3)

    mock_boto3.resource.assert_called_with('s3', region_name='us-east-1')
    mock_boto3.resource().Bucket.assert_called_with('bucket')
    mock_boto3.resource().Bucket().objects.filter.assert_called_with(Prefix='prefix/')

def test_download_folder(mock_boto3):
    response = socks.s3.download_folder('bucket', 'prefix/', 'local_path', session=mock_boto3)

    mock_boto3.client.assert_called_with('s3', region_name='us-east-1')
    mock_boto3.client().get_paginator.assert_called_with('list_objects')

def test_object_exists(mock_boto3):
    response = socks.s3.object_exists('bucket', 'prefix/object.txt', session=mock_boto3)

    mock_boto3.resource.assert_called_with('s3', region_name='us-east-1')
    mock_boto3.resource().Object.assert_called_with('bucket', 'prefix/object.txt')
    mock_boto3.resource().Object().load.assert_called()