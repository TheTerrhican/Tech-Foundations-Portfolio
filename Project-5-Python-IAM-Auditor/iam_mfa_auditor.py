import boto3
import json
import sys

# Initialize the IAM client
# NOTE: This script assumes you have configured AWS credentials locally
try:
    iam = boto3.client('iam')
except Exception as e:
    print(f"Error initializing Boto3 client. Check AWS credentials: {e}")
    # Exit gracefully if AWS credentials aren't found, as the script won't run.
    sys.exit(1)

def audit_mfa_status():
    """Checks all IAM users in the account for missing Multi-Factor Authentication (MFA)."""
    
    print("--- Starting IAM MFA Audit ---")
    
    # Stores users missing MFA
    users_missing_mfa = []
    
    try:
        # Paginator handles fetching a large list of users from the AWS API
        paginator = iam.get_paginator('list_users')
        pages = paginator.paginate()

        for page in pages:
            for user in page['Users']:
                username = user['UserName']
                
                # Check for virtual MFA devices
                virtual_mfa = iam.list_virtual_mfa_devices(
                    AssignmentStatus='Assigned',
                    UserName=username
                )
                
                # Check for hardware MFA devices
                mfa_devices = iam.list_mfa_devices(UserName=username)
                
                # Logic: If both lists are empty, MFA is missing.
                if not virtual_mfa['VirtualMFADevices'] and not mfa_devices['MFADevices']:
                    users_missing_mfa.append(username)
                    print(f"[ALERT] User '{username}' is missing MFA.")

    except Exception as e:
        print(f"\n[FATAL ERROR] An error occurred during the audit: {e}")
        # Return without generating a summary if a major error occurred
        return

    # Generate Final Report
    print("\n--- AUDIT SUMMARY ---")
    if users_missing_mfa:
        print(f"❗ {len(users_missing_mfa)} User(s) REQUIRE IMMEDIATE ATTENTION:")
        for user in users_missing_mfa:
            print(f"- {user}")
    else:
        print("✅ ALL IAM users have MFA enabled. Security posture is good.")
    
if __name__ == "__main__":
    audit_mfa_status()