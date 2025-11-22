# s3_auditor.py - Python Script for Project 7

import boto3
import json

# Initialize Boto3 S3 Client (Requires local AWS credentials setup)
try:
    s3 = boto3.client('s3')
except Exception as e:
    # This failure is expected if no live credentials are set, which is a key security takeaway.
    print(f"Error: Could not initialize S3 client. Check AWS credentials. Error: {e}")
    exit()

def audit_s3_buckets():
    """Scans all S3 buckets for security and configuration violations."""
    
    print("--- Starting S3 Security Audit ---")
    violations = []
    
    try:
        # Get list of all buckets
        response = s3.list_buckets()
        buckets = response.get('Buckets', [])
        
        if not buckets:
            print("No S3 buckets found in this account.")
            return

        for bucket in buckets:
            name = bucket['Name']
            bucket_violations = []

            # Check 1: Public Access Configuration (Critical)
            try:
                public_access_status = s3.get_public_access_block(Bucket=name)
                if not public_access_status['PublicAccessBlockConfiguration'].get('BlockPublicAcls') or \
                   not public_access_status['PublicAccessBlockConfiguration'].get('BlockPublicPolicy'):
                    bucket_violations.append("Public Access NOT Fully Blocked")
            except Exception:
                bucket_violations.append("Missing Public Access Block Configuration")

            # Check 2: Encryption (At Rest)
            try:
                s3.get_bucket_encryption(Bucket=name)
            except s3.exceptions.ClientError:
                bucket_violations.append("Missing Default Encryption (SSE-S3/KMS)")

            # Check 3: Versioning (Disaster Recovery/Compliance)
            versioning = s3.get_bucket_versioning(Bucket=name)
            if versioning.get('Status') != 'Enabled':
                bucket_violations.append("Versioning Not Enabled (DR Risk)")

            if bucket_violations:
                violations.append({
                    'BucketName': name,
                    'Violations': bucket_violations
                })

    except Exception as e:
        print(f"\n[FATAL ERROR] An error occurred during the audit: {e}")
        return

    # Generate Final Report
    print("\n--- AUDIT SUMMARY REPORT ---")
    if violations:
        print(f"❗ {len(violations)} Buckets REQUIRE IMMEDIATE ATTENTION.")
    else:
        print("✅ ALL S3 buckets are compliant with security baselines.")

if __name__ == "__main__":
    audit_s3_buckets()
