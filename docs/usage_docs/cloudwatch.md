# CloudWatch {docsify-ignore}

## socks.cloudwatch.get_sequence_token
Gets the next sequence token for pushing a log to a cloudwatch group.  

### Parameters
<table>
<tr>
  <td>group_name (string)<br/>
    <i>Required</i>
  </td>
  <td>The name of the cloudwatch group</td>
</tr>
<tr>
  <td>stream_name (string)<br/>
    <i>Required</i>
  </td>
  <td>The name of the stream in the cloudwatch group to get the sequence token for</td>
</tr>
<tr>
  <td>session (Session)<br/>
    <i>Optional</i>
  </td>
  <td>Boto3 session to use - useful when assuming sessions in other accounts. Default is the default boto3 session.</td>
</tr>
<tr>
  <td>region_name (string)<br/>
    <i>Optional</i>
  </td>
  <td>Region for boto3 to use. Default is "us-east-1"</td>
</tr>
</table>  
  
### Returns
Returns the requested sequence token. Returns None in the case of an error.  

### Example
Placeholder
<br/>
<br/>

## socks.cloudwatch.push_json_log  
Push a custom log dict/object to a cloudwatch group/sequence  

### Parameters  
<table>
<tr>
  <td>log_body (dict)<br/>
    <i>Required</i>
  </td>
  <td>The log object to be pushed to the cloudwatch stream</td>
</tr>
<tr>
  <td>group_name (string)<br/>
    <i>Required</i>
  </td>
  <td>The name of the cloudwatch group that contains the log stream</td>
</tr>
<tr>
  <td>stream_name (string)<br/>
    <i>Required</i>
  </td>
  <td>The name of the cloudwatch stream to send the log to</td>
</tr>
<tr>
  <td>session (Session)<br/>
    <i>Optional</i>
  </td>
  <td>Boto3 session to use - useful when assuming sessions in other accounts. Default is the default boto3 session.</td>
</tr>
<tr>
  <td>region_name (string)<br/>
    <i>Optional</i>
  </td>
  <td>Region for boto3 to use. Default is "us-east-1"</td>
</tr>
<tr>
  <td>**cw_client_put_log_events_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.put_log_events">Cloudwatch Client put_log_events() method</a></td>
</tr>
</table>     

### Returns
Returns the requested sequence token. Returns None in the case of an error.

### Example
Placeholder