import boto3

iam = boto3.client('iam')

role_name = 'EC2AccessRole'
policy_arn = 'arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess'

# Attach the policy to the role
response = iam.attach_role_policy(
    RoleName=role_name,
    PolicyArn=policy_arn
)

print(f"Policy '{policy_arn}' attached to role '{role_name}'")
