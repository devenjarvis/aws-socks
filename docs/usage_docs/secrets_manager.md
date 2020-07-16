# Secrets Manager {docsify-ignore}

## socks.secretsmanager.env  
A helper function to specify environment specific secrets.

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

## socks.secretsmanager.get_secret
Gets a secret from AWS Secrets Manager

### Parameters
<table>
<tr>
  <td>secret_name (string)<br/>
    <i>Required</i>
  </td>
  <td>The name of the secret to be retrieved.</td>
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
  <td>**secrets_client_get_secret_value_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.get_secret_value">Secrets Manager Client get_secret_value() method</a></td>
</tr>
</table>  

### Returns  
The SecretString or SecretBinary depending on the secret type.

### Examples
Placeholder