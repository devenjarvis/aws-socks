import boto3
import socks.s3
import time, csv, os

def query(sql_statement, database, bucket, key='results', local_filepath=None, workgroup=None, session=boto3, region_name='us-east-1', **athena_start_query_execution_kwargs):
    athena_client = session.client('athena', region_name=region_name) 

    athena_start_query_execution_kwargs['QueryString'] = sql_statement
    if 'QueryExecutionContext' in athena_start_query_execution_kwargs:
        athena_start_query_execution_kwargs['QueryExecutionContext']['Database'] = database
    else:
        athena_start_query_execution_kwargs['QueryExecutionContext'] = {'Database': database}

    if 'ResultConfiguration' in athena_start_query_execution_kwargs:
        athena_start_query_execution_kwargs['ResultConfiguration']['OutputLocation'] = f"s3://{bucket}/{key}"
    else:
        athena_start_query_execution_kwargs['ResultConfiguration'] = {'OutputLocation': f"s3://{bucket}/{key}"}

    if workgroup:
        athena_start_query_execution_kwargs['WorkGroup']=workgroup


    start_query_response = athena_client.start_query_execution(**athena_start_query_execution_kwargs)
    execution_id = start_query_response['QueryExecutionId']
    
    #Check State of Query, Continue Waiting Until State is 'SUCCEEDED', 'FAILED', or 'CANCELLED'
    while True:
        stats = athena_client.get_query_execution(QueryExecutionId = execution_id)
        status = stats['QueryExecution']['Status']['State']
        if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            break
        time.sleep(0.2)  # 200ms

    if status == 'SUCCEEDED':
        #Attempt to Make New Local Directory if Doesn't Exist
        if local_filepath:
            os.makedirs(os.path.dirname(local_filepath), exist_ok=True)
            
            if socks.s3.object_exists(bucket, f"{key}/{execution_id}.csv", session, region_name):
                socks.s3.download_file(local_filepath, bucket, f"{key}/{execution_id}.csv", session, region_name)
                with open(local_filepath) as f:
                    data = [{k: v for k,v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
                
                return data
            elif socks.s3.object_exists(bucket, f"{key}/{execution_id}.txt", session, region_name):
                socks.s3.download_file(local_filepath, bucket, f"{key}/{execution_id}.txt", session, region_name)
                with open(local_filepath) as f:
                    data = f.read()
                
                return data
            else:
                print(f"ERROR: Athena query did not succeed and ended with state {status['State']} because {status['StateChangeReason']}")
                return None
        else:
            return True
    elif status == 'FAILED':
        status = athena_client.get_query_execution(QueryExecutionId = execution_id)['QueryExecution']['Status']
        print(f"ERROR: Athena query did not succeed and ended with state {status['State']} because {status['StateChangeReason']}")
        return None
    elif status == 'CANCELLED':
        print("INFO: Athena query was cancelled")
        return None