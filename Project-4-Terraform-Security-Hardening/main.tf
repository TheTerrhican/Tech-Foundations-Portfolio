# main.tf - Terraform Configuration File for Project 4

# 1. Define the AWS Provider
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# 2. Configure AWS Provider (using default credentials/region)
provider "aws" {
  region = "us-east-1" # Or any region you choose
}

# 3. Define the Security Group (The Virtual Firewall)
resource "aws_security_group" "web_server_sg" {
  name        = "portfolio-web-server-sg"
  description = "Allows secure web traffic and restricted admin access."
  vpc_id      = "vpc-0abc12345def" # NOTE: Replace with a placeholder VPC ID or a variable

  # Inbound Rule 1: HTTPS (Secure Web Traffic)
  ingress {
    description = "Allow HTTPS from anywhere"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Inbound Rule 2: SSH (Admin Access) - Following PoLP!
  ingress {
    description = "Allow SSH from specific admin IP"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    # BEST PRACTICE: This demonstrates restricting SSH access for security.
    cidr_blocks = ["203.0.113.1/32"] 
  }

  # Outbound Rule: Default (Allows all outbound traffic)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # -1 means all protocols
    cidr_blocks = ["0.0.0.0/0"]
  }
}
