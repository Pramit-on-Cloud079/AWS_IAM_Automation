import boto3

# Initialize IAM client
iam = boto3.client('iam')

# Group and user details
group_name = 'Admins'
user_name = 'test-user'

# Create the group
group_response = iam.create_group(GroupName=group_name)
print("Group Created:", group_response['Group']['GroupName'])

# Add user to group
add_response = iam.add_user_to_group(
    GroupName=group_name,
    UserName=user_name
)
print(f"User '{user_name}' added to group '{group_name}'")
