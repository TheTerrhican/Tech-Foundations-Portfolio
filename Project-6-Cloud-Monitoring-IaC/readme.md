# 👁️ Project 6: Automated Cloud Monitoring (Terraform IaC)

## 🎯 Focus Area
**Observability, Infrastructure as Code (IaC), and Incident Alerting (DevOps/SRE)**

## 💡 Overview
This project deploys a complete, operational monitoring stack using **Terraform**. It demonstrates setting up **Synthetic Monitoring** (active checks of a live endpoint), defining **CloudWatch Alarms**, and integrating with **SNS** for automated notification upon failure. This establishes a baseline for **Incident Response (IR)** and operational maturity.

## ⚙️ Technologies & Concepts Demonstrated
* **Terraform (HCL):** Used to define the entire infrastructure stack (Canary, IAM Role, SNS, Alarm).
* **Cloud Observability:** Implementing active health checks using **AWS Synthetics Canary**.
* **Security (IAM):** Defining a minimal permission **IAM Role** for the Canary, adhering to the **Principle of Least Privilege (PoLP)**.
* **Incident Alerting:** Linking an alarm condition (`SuccessRate < 100%`) to an **SNS Topic** to initiate automated notifications.

## 📝 The Architecture Workflow
1.  **aws_synthetics_canary:** A scheduled, serverless script actively checks the target URL (Project 3 site) every 5 minutes.
2.  **CloudWatch Metric Alarm:** Watches the Canary's `SuccessRate` metric. If the rate drops below 100% (failure), the alarm is triggered instantly.
3.  **aws_sns_topic:** The triggered alarm sends a notification (configured as an email) to the defined administrator.

## ⚠️ Note on Deployment
The successful deployment of this project requires the user to manually create the `canary.zip` file (containing the monitoring script) and configure AWS credentials locally, reinforcing hands-on CI/CD pipeline skills.
