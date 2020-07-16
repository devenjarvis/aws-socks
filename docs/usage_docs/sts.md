# STS {docsify-ignore}


## socks.sts.assume_role  
Assume another IAM role. Useful for cross-account access.

### Parameters  
<table>
<tr>
  <td>arn (string)<br/>
    <i>Required</i>
  </td>
  <td>The arn of the role you want to assume</td>
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
  <td>**sts_client_assume_role_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.assume_role">STS Client assume_role() method</td>
</tr>
</table>

### Returns  
Returns a new session that can then be passed into any other socks function to perform it as the assumed role.

### Examples
Placeholder