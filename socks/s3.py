import boto3
from botocore.exceptions import ClientError
import json, csv, os

#TODO: Are there other common object types that should be supported?
#TODO: Write a unit test
def read_file(bucket, key, encoding='utf-8', session=boto3, region_name='us-east-1', **s3_object_get_kwargs):
    s3_resource = session.resource('s3', region_name=region_name)
    s3_object = s3_resource.Object(bucket, key)

    try:
        content = s3_object.get(**s3_object_get_kwargs)['Body'].read().decode(encoding)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        object_format = key.split('.')[-1]
        if object_format == 'json':
            json_content = json.loads(content)
            return json_content
        elif object_format == 'csv':
            return csv.DictReader(content.split())
        else:
            return content

#TODO: Add checking for local filepath.
#TODO: Add error handling.
#TODO: Write a unit test
def download_file(local_path, bucket, key, session=boto3, region_name='us-east-1', **s3_object_download_fileobj_kwargs):
    s3_resource = session.resource('s3', region_name=region_name)
    s3_object = s3_resource.Object(bucket, key)

    try:
        with open(local_path, 'wb') as fileobj:
            #Set kwargs
            s3_object_download_fileobj_kwargs['Fileobj'] = fileobj
            
            response = s3_object.download_fileobj(**s3_object_download_fileobj_kwargs)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        return response

#TODO: Add error handling
#TODO: Write a unit test
def write_file(content, bucket, key, session=boto3, region_name='us-east-1', **s3_object_put_kwargs):
    s3_resource = session.resource('s3', region_name=region_name)
    s3_object = s3_resource.Object(bucket, key)
    object_format = key.split('.')[-1]

    #Set kwargs
    s3_object_put_kwargs['Body'] = content

    try:
        response = s3_object.put(**s3_object_put_kwargs)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        return response

#TODO: Add error handling.
#TODO: Write a unit test
def upload_file(local_path, bucket, key, session=boto3, region_name='us-east-1', **s3_object_upload_file_kwargs):
    s3_resource = session.resource('s3', region_name=region_name)
    s3_object = s3_resource.Object(bucket, key)

    #Set kwargs
    s3_object_upload_file_kwargs['Filename'] = local_path

    try:
        response = s3_object.upload_file(**s3_object_upload_file_kwargs)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        return response

#TODO: Error handling
#TODO: Write a unit test
def delete_file(bucket, key, session=boto3, region_name='us-east-1', **s3_object_delete_kwargs):
    s3_resource = session.resource('s3', region_name=region_name)
    s3_object = s3_resource.Object(bucket, key)

    try:
        response = s3_object.delete(**s3_object_delete_kwargs)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        return response 

#TODO: Error handling
#TODO: Add parameter to return folders as well
#TODO: Write a unit test
def list_files(bucket, prefix, session=boto3, region_name='us-east-1', **s3_bucket_objects_filer_kwargs):
    s3_resource = session.resource('s3', region_name=region_name)
    s3_bucket = s3_resource.Bucket(bucket)

    #Set kwargs
    s3_bucket_objects_filer_kwargs['Prefix'] = prefix

    try:
        objects = s3_bucket.objects.filter(**s3_bucket_objects_filer_kwargs)
    except ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"ERROR: {error_code}")
        raise e
    else:
        return [object_summary.key for object_summary in objects if object_summary.key[-1] != '/']

#TODO: Return something
#TODO: Error Handling
#TODO: Write a unit test
def download_folder(bucket, prefix, local_path, session=boto3, region_name='us-east-1', **s3_client_download_file_kwargs):
    s3_client = session.client('s3', region_name=region_name)

    paginator = s3_client.get_paginator('list_objects')
    for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=prefix):
        if result.get('CommonPrefixes') is not None:
            for subdir in result.get('CommonPrefixes'):
                download_folder(bucket, subdir.get('Prefix'), local_path)
        if result.get('Contents') is not None:
            for file in result.get('Contents'):
                if not os.path.exists(os.path.dirname(local_path + os.sep + file.get('Key'))):
                    os.makedirs(os.path.dirname(local_path + os.sep + file.get('Key')))
                if not file.get('Key').endswith('/'):
                    #Set kwargs
                    s3_client_download_file_kwargs['Bucket'] = bucket
                    s3_client_download_file_kwargs['Key'] = file.get('Key')
                    s3_client_download_file_kwargs['Filename'] = local_path + os.sep + file.get('Key')
                    s3_client.download_file(**s3_client_download_file_kwargs)


def object_exists(bucket, key, session=boto3, region_name='us-east-1'):
    s3_resource = session.resource('s3', region_name=region_name)

    try:
        s3_resource.Object(bucket, key).load()
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == "404":
            return False
        else:
            print(f"ERROR: {error_code}")
            raise e
    else:
        return True