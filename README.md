## IaC
I used Terraform as that is what I have experience in, that would be the quickest to write.
To provisoun run the following:
```bash
terraform apply
```

## Deploying
Terraform will take care of packaging the `main.py` file and pushing it to Lambda, just need to run:
```
terraform apply
```

## VPC
Terraform will create a VPC and subnet to use an existing VPC edit the `vpc_config` property of `aws_lambda_function.snapshot_cleanup` with the appropriate subnet ids and security group ids of desired VPC.

## Assumptions
The following are assumed and can be changed by setting variable value.
 - function_name=lambda_snapshot_cleanup
 - region=us-east-1


## Monitoring 

By attaching AWSLambdaBasicExecutionRole to the IAM execution role we are able to monitor thorugh `Amazon CLoudWatcher` logs.

## Diagram
![diagram](lambda.drawio.png)