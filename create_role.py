import boto3
import json

iam = boto3.client('iam')

role_name = 'EC2AccessRole'

# Trust relationship policy document for EC2
assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

# Create the IAM role
response = iam.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=json.dumps(assume_role_policy),
    Description='Allows EC2 to assume this role'
)

print("Role created:")
print("Role Name:", response['Role']['RoleName'])
print("ARN:", response['Role']['Arn'])
