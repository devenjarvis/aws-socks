# SSM (Parameter Store) {docsify-ignore}


## socks.ssm.env
A helper function to specify environment specific parameters.

### Parameters  
<table>
<tr>
  <td>env (string)<br/>
    <i>Required</i>
  </td>
  <td>The environment name to prepend to each parameter requested</td>
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
Return an instance of the Env class. 

### Examples
Placeholder
<br/>
<br/>

## socks.ssm.get_parameter
Gets a parameter from SSM with the provided parameter name

### Parameters
<table>
<tr>
  <td>name (string)<br/>
    <i>Required</i>
  </td>
  <td>The name of the SSM parameter (without the prepended environment name)</td>
</tr>
<tr>
  <td>encrypted (boolean)<br/>
    <i>Optional</i>
  </td>
  <td>Whether or not the requested parameter is encrypted with a KMS key</td>
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
  <td>**ssm_client_get_parameter_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_parameter">SSM Client get_parameter() method</a></td>
</tr>
</table>  

### Returns  
Returns the value stored for this parameter

### Examples
Placeholder