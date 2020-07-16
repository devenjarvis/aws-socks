# Athena {docsify-ignore}

##  socks.athena.query
Executes a SQL statement against Athena and returns the results as an array of dictionaries.  

### Parameters
<table>
<tr>
  <td>sql_statement (string)<br/>
    <i>Required</i>
  </td>
  <td>The SQL statement to be executed.</td>
</tr>
<tr>
  <td>database (string)<br/>
    <i>Required</i>
  </td>
  <td>The Athena database the query will be executed against.</td>
</tr>
<tr>
  <td>bucket (string)<br/>
    <i>Required</i>
  </td>
  <td>The S3 bucket Athena will write the resulting .csv to.</td>
</tr>
<tr>
  <td>key (string)<br/>
    <i>Required</i>
  </td>
  <td>The path in the S3 bucket Athena will prefix to the resulting .csv.</td>
</tr>
<tr>
  <td>local_filepath (string)<br/>
    <i>Optional</i>
  </td>
  <td>Where to save the resulting .csv file locally before loading into memory.</td>
</tr>
<tr>
  <td>workgroup (string)<br/>
    <i>Optional</i>
  </td>
  <td>Workgroup to execute your Athena query in. Default is the primary workgroup (aka no workgroup).</td>
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
  <td>**athena_start_query_execution_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.start_query_execution">Athena Client .start_query_execution() method</a></td>
</tr>
</table>    

### Return
If a local_filepath is given, an array of dicts with each dict representing a row returned from Athena. Column names are used for the dict keys. 
Otherwise, the function returns 1 on success.
Returns None in case of error.

### Example
Placeholder