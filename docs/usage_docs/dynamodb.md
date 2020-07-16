# DynamoDB {docsify-ignore}

## socks.dynamodb.add_item   
Adds a new item to a Dynamodb table 

### Parameters
<table>
<tr>
  <td>table_name (string)<br/>
    <i>Required</i>
  </td>
  <td>The name of the dynamodb table</td>
</tr>
<tr>
  <td>item (dict)<br/>
    <i>Required</i>
  </td>
  <td>The object to add to the dynamo table</td>
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
  <td>**dynamo_table_put_item_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.put_item">DynamoDB Table put_item() method</a></td>
</tr>
</table> 

### Return
The response from the put_item operation 

### Examples
Placeholder
<br/>
<br/>

## socks.dynamodb.update_item <a name="socks.dynamodb.update_item"></a>  
Updates an existing item to a Dynamodb table, or adds it if it doesn't exist already

### Parameters
<table>
<tr>
  <td>table_name (string)<br/>
    <i>Required</i>
  </td>
  <td>The name of the dynamodb table</td>
</tr>
<tr>
  <td>key (dict)<br/>
    <i>Required</i>
  </td>
  <td>An object containing the key and value of the primary key for the record you want to update</td>
</tr>
<tr>
  <td>item (dict)<br/>
    <i>Required</i>
  </td>
  <td>An object containing the keys and values you want to update for this item.</td>
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
  <td>**dynamo_table_update_item_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.update_item">DynamoDB Table update_item() method</a></td>
</tr>
</table> 

### Returns
The response from the update_item operation 

### Examples
Placeholder
<br/>
<br/>

## socks.dynamodb.get_item <a name="socks.dynamodb.get_item"></a>  
Retrieves an item from a Dynamo table

### Parameters
<table>
<tr>
  <td>table_name (string)<br/>
    <i>Required</i>
  </td>
  <td>The name of the dynamodb table</td>
</tr>
<tr>
  <td>key (dict)<br/>
    <i>Required</i>
  </td>
  <td>An object containing the key and value of the primary key for the record you want to get</td>
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
  <td>**dynamo_table_get_item_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.get_item">DynamoDB Table get_item() method</a></td>
</tr>
</table>  

### Returns
A dict of the item requested from dynamo.

### Examples
Placeholder
<br/>
<br/>

## socks.dynamodb.delete_item <a name="socks.dynamodb.delete_item"></a>  
Deletes an item from a Dynamo table

### Parameters
<table>
<tr>
  <td>table_name (string)<br/>
    <i>Required</i>
  </td>
  <td>The name of the dynamodb table</td>
</tr>
<tr>
  <td>key (dict)<br/>
    <i>Required</i>
  </td>
  <td>An object containing the key and value of the primary key for the record you want to delete</td>
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
  <td>**dynamo_table_delete_item_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.delete_item">DynamoDB Table delete_item() method</a></td>
</tr>
</table>   

### Returns
The response from the delete_item operation

### Examples
Placeholder
<br/>
<br/>


## socks.dynamodb.query_table <a name="socks.dynamodb.query_table"></a>  
Executes and returns the results of a query on dynamodb

### Parameters
<table>
<tr>
  <td>table_name (string)<br/>
    <i>Required</i>
  </td>
  <td>The name of the dynamodb table</td>
</tr>
<tr>
  <td>key_condition_expression (dict)<br/>
    <i>Required</i>
  </td>
  <td>The KeyCondition dictionary containing the query you want to execute</td>
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
  <td>**dynamo_table_query_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.query">DynamoDB Table query() method</a></td>
</tr>
</table> 

### Returns
A list of dictionaries, where each element represents an object returned from your query

### Examples
Placeholder
<br/>
<br/>

## socks.dynamodb.scan_table <a name="socks.dynamodb.scan_table"></a>  
Scans a Dyanmo table and returns all items.

### Parameters
<table>
<tr>
  <td>table_name (string)<br/>
    <i>Required</i>
  </td>
  <td>The name of the dynamodb table</td>
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
  <td>**dynamo_table_scan_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.scan">DynamoDB Table scan() method</a></td>
</tr>
</table>

### Returns
Returns the response of boto3 Dynamo scan operation

### Examples
Placeholder