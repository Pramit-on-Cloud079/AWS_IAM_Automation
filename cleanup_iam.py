import boto3
from botocore.exceptions import ClientError

iam = boto3.client('iam')

user_name = 'test-user'
role_name = 'EC2AutomationRole'
policy_arn = 'arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess'
group_name = 'Admins'

# Detach policy from role
try:
    iam.detach_role_policy(RoleName=role_name, PolicyArn=policy_arn)
    print("✅ Policy detached from role")
except ClientError as e:
    print(f"❌ Error detaching policy: {e}")

# Delete the IAM role
try:
    iam.delete_role(RoleName=role_name)
    print("✅ IAM role deleted")
except ClientError as e:
    print(f"❌ Error deleting role: {e}")

# Remove user from group
try:
    iam.remove_user_from_group(GroupName=group_name, UserName=user_name)
    print("✅ User removed from group")
except ClientError as e:
    print(f"❌ Error removing user from group: {e}")

# Delete login profile (console access)
try:
    iam.delete_login_profile(UserName=user_name)
    print("✅ Login profile deleted")
except ClientError as e:
    print(f"❌ No login profile to delete or error: {e}")

# Delete the user
try:
    iam.delete_user(UserName=user_name)
    print("✅ User deleted")
except ClientError as e:
    print(f"❌ Error deleting user: {e}")
