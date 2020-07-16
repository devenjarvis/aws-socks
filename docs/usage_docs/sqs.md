# SQS {docsify-ignore}

## socks.sqs.send_message
Pushes a message to an SQS queue  

### Parameters 
<table>
<tr>
  <td>message (dict)<br/>
    <i>Required</i>
  </td>
  <td>The dict/object to be stringified and sent to SQS</td>
</tr>
<tr>
  <td>queue_url (string)<br/>
    <i>Required</i>
  </td>
  <td>The url of the SQS queue.</td>
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
  <td>**sqs_client_send_message_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.send_message">SQS Client send_message() method</a></td>
</tr>
</table>  

### Returns  
The response from boto3 send_message operation 

### Examples
Placeholder 
<br/>
<br/>

## socks.sqs.receive_message 
Retrieves a message from an SQS queue.  

### Parameters 
<table>
<tr>
  <td>queue_url (string)<br/>
    <i>Required</i>
  </td>
  <td>The URL of the SQS queue you want to get the message from.</td>
</tr>
<tr>
  <td>max_num_messages (integer)<br/>
    <i>Required</i>
  </td>
  <td>The number of messages you'd like to retrieve.</td>
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
  <td>**sqs_client_receive_message_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.receive_message">SQS Client receive_message() method</a></td>
</tr>
</table>  

### Returns  
The message as a string and the receipt handle to be used for deleting the message. 

### Examples
Placeholder
<br/>
<br/>

## socks.sqs.delete_message 
Deletes a message from an SQS queue.  

### Parameters  
<table>
<tr>
  <td>queue_url (string)<br/>
    <i>Required</i>
  </td>
  <td>The URL of the SQS queue you want to delete the message from</td>
</tr>
<tr>
  <td>receipt_handle (string)<br/>
    <i>Required</i>
  </td>
  <td>The receipt handle of the message you'd like to delete</td>
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
  <td>**sqs_client_delete_message_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.delete_message">SQS Client delete_message() method</a></td>
</tr>
</table>  

### Returns  
The response from the delete_message operation. 

### Examples
Placeholder