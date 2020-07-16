# Lambda {docsify-ignore}

## socks.aws_lambda.invoke_lambda_function <a name="socks.aws_lambda.invoke_lambda_function"></a>  
Invoke an AWS Lambda function 

### Parameters  
<table>
<tr>
  <td>function_name (string)<br/>
    <i>Required</i>
  </td>
  <td>The Name of the Lambda Function you want to Invoke</td>
</tr>
<tr>
  <td>pay_load (dict)<br/>
    <i>Required</i>
  </td>
  <td>Input Event/paylod for any lambda to be invoked.</td>
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
  <td>**lambda_client_invoke_kwargs<br/>
    <i>Optional</i>
  </td>
  <td>Supports boto3 keyword arguments for <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.invoke">Lambda Client invoke() method</a></td>
</tr>
</table>     

### Returns
Returns response from the boto3 invoke operation.

### Example
Placeholder