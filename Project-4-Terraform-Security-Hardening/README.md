# 🔒 Project 4: Automated Security Group Hardening (Terraform IaC)

## 🎯 Focus Area
**Infrastructure as Code (IaC), Cloud Security, and Automation**

## 💡 Overview
This project demonstrates the use of **Terraform** to define and deploy foundational cloud network security controls. By writing infrastructure as code, we ensure the deployment of an AWS Security Group adheres strictly to the **Principle of Least Privilege (PoLP)**, making the network environment auditable and easily reproducible.

## ⚙️ Technologies & Concepts Demonstrated
* **Terraform (HCL):** Used to define the infrastructure state.
* **Infrastructure as Code (IaC):** Managing infrastructure via code for consistency and version control.
* **AWS Security Groups:** Acting as stateful virtual firewalls to control traffic flow.
* **Principle of Least Privilege (PoLP):** Only opening the bare minimum ports (443 and restricted 22) required for the server function.
* **Network Segmentation:** Using ingress and egress rules to control the attack surface.

## 📝 The Implementation
The `main.tf` file defines a Security Group for a typical public-facing web server:

1.  **Ingress (Inbound):** Only TCP ports **443 (HTTPS)** are open to the world (`0.0.0.0/0`). **TCP Port 22 (SSH)** is restricted to a single, specific administrative IP address (`203.0.113.1/32`).
2.  **Egress (Outbound):** All traffic is allowed outbound, which is common for web servers that need to connect to backend services or APIs.

## 🚀 Deployment Process (Conceptual)
1.  `terraform init`: Initializes the working directory.
2.  `terraform plan`: Shows exactly what infrastructure changes will be made (Audit step).
3.  `terraform apply`: Executes the code, creating the secure Security Group in AWS.
4.  `terraform destroy`: Cleans up the resources to prevent unnecessary costs.

---
