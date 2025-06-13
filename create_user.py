import boto3

# Initialize IAM client
iam = boto3.client('iam')

# User details
user_name = 'test-user'

# Create the user
response = iam.create_user(UserName=user_name)

# Print user details
print("User Created:")
print("Username:", response['User']['UserName'])
print("ARN:", response['User']['Arn'])
