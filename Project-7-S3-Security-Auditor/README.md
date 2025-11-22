# 🐍 Project 7: Automated S3 Bucket Security Auditor (Python/Boto3)

## 🎯 Focus Area
**Cloud Security Policy, Data Governance, and Python Automation**

## 💡 Overview
This project develops a scalable **Python script** that uses the **AWS SDK (Boto3)** to scan all S3 buckets in an account for critical security and data governance violations. This simulates a common task for **Cloud Security Engineers** and ensures data is protected against public exposure and loss. The value is in the **source code and security policy logic**, which is executed locally to demonstrate API interaction capability.

## ⚙️ Technologies & Concepts Demonstrated
* **Python/Boto3:** Extensive use of the S3 client API to retrieve security and configuration data (e.g., `get_public_access_block`, `get_bucket_encryption`).
* **Cloud Security Policy:** Auditing for fundamental compliance rules: **Public Access Block**, **Default Encryption**, and **Versioning**.
* **Security Automation:** Building a tool for continuous security monitoring instead of relying on manual console checks.
* **API Interaction:** Demonstrating ability to write code that interacts with cloud provider APIs, a critical skill for any cloud role.

## 📝 The Implementation (Policy Logic)
The `s3_auditor.py` script checks every discovered S3 bucket for three high-risk findings:

1.  **Public Exposure:** Verifies that Public Access Block policies are fully enforced.
2.  **Encryption:** Checks that default server-side encryption is enabled to protect data at rest.
3.  **Versioning:** Ensures Versioning is enabled, mitigating data loss from accidental deletion (Disaster Recovery).

## ⚠️ Execution Note
This project demonstrates **functional API code**. Execution requires AWS credentials to be configured locally (e.g., via `aws configure` or environment variables) and sufficient IAM permissions to list and inspect S3 buckets. The script is designed to fail gracefully if required credentials are not found.
