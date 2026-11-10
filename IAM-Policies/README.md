## Least-privilege permissions

Replace the placeholders before use: `111122223333` (AWS account ID), `us-west-2` (Region),
`amzn-s3-demo-bucket` (your S3 bucket), and
`your-domain-name` (your OpenSearch Service domain). Do not attach AWS managed `*FullAccess`
policies or map the Lambda role to the OpenSearch `all_access` role.

| File | Attach to |
|------|-----------|
| `s3copybookparser-policy.json` | IAM role of the `s3copybookparser` Lambda function |
| `s3toathena-policy.json` | IAM role of the `s3toathena` Lambda function |
| `s3toelasticsearch-policy.json` | IAM role of the `s3toelasticsearch` Lambda function |

Also attach the `AWSLambdaBasicExecutionRole` managed policy to each Lambda role for CloudWatch Logs.

### OpenSearch fine-grained access control

The Lambda function only creates indexes (named after the data file, for example `employee.csv`)
and bulk-writes documents. Create a dedicated role and map the Lambda IAM role to it instead of `all_access`:

```
PUT _plugins/_security/api/roles/fileviewer_lambda_writer
<contents of opensearch-lambda-role.json>

PUT _plugins/_security/api/rolesmapping/fileviewer_lambda_writer
<contents of opensearch-lambda-rolemapping.json>
```
