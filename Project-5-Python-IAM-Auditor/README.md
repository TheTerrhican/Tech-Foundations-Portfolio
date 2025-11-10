# 🐍 Project 5: Python and Boto3 IAM MFA Auditor

## 🎯 Focus Area
**Cloud Security, Automation, and Identity & Access Management (IAM)**

## 💡 Overview
This project uses **Python** and the **AWS SDK (Boto3)** to automate a critical security audit task: verifying Multi-Factor Authentication (MFA) enforcement for all IAM users in an AWS account. This demonstrates ability to create **Security Automation Tools** essential for maintaining a secure cloud environment.

## ⚙️ Technologies & Concepts Demonstrated
* **Python/Boto3:** Integration with AWS API for automated data retrieval.
* **Cloud Security:** Deep understanding of **IAM** and the critical nature of **MFA** for account security.
* **Automation:** Moving from manual console checks to scalable, scripted verification.
* **Security Audit:** Performing a specific, high-priority compliance check.

## 📝 The Implementation
The `iam_mfa_auditor.py` script performs the following steps:

1.  Initializes the `boto3` IAM client (requires configured AWS credentials).
2.  Uses the IAM `list_users` paginator to fetch all user accounts.
3.  For each user, it queries both `list_virtual_mfa_devices` and `list_mfa_devices` to check for assigned MFA tokens.
4.  Generates a clear report flagging all users who are missing this essential layer of security.

## 🚀 Impact
This tool provides immediate visibility into the most common human-factor security risk, allowing security teams to enforce compliance and adhere to frameworks like the **AWS Well-Architected Framework**.
