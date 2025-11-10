# main.tf - Deploys a Serverless Monitoring Stack for Observability

# -----------------
# 1. AWS Provider and Variables
# -----------------

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1" # Standard region for simplicity
}

# Define your live project URL and project name
locals {
  target_url   = "https://my-portfolio-site-kk1.pages.dev" # Your Project 3 URL (Replace if needed)
  project_name = "portfolio-site-monitor"
  
  # Base64 encoded JavaScript code for the Canary check (simplest form)
  canary_script_content = <<-EOT
    var synthetics = require('Synthetics');
    const log = require('SyntheticsLogger');
    const pageUrl = 'https://my-portfolio-site-kk1.pages.dev'; 

    const checkWebsite = async function() {
        // Ensure the website returns a 200 OK status code
        let response = await synthetics.getPage(pageUrl, {
            'headers': {
                'User-Agent': 'CloudWatch Synthetics Canary'
            }
        });

        if (response.statusCode != 200) {
            throw new Error('Website check failed with status code: ' + response.statusCode);
        }
        log.info('Website check successful with status 200.');
    };

    exports.handler = async () => {
        return await checkWebsite();
    };
EOT
}

# -----------------
# 2. Notification Service (SNS)
# -----------------

# SNS Topic: This is the destination for the alarm notification
resource "aws_sns_topic" "alert_topic" {
  name = "${local.project_name}-alert-topic"
}

# Subscription: **REPLACE WITH YOUR EMAIL** to receive alerts
resource "aws_sns_topic_subscription" "email_subscription" {
  topic_arn = aws_sns_topic.alert_topic.arn
  protocol  = "email"
  endpoint  = "your.email@example.com" # <--- REPLACE THIS EMAIL ADDRESS
  # IMPORTANT: You must manually confirm the subscription email after deployment!
}

# -----------------
# 3. IAM Role for Synthetics Canary (Least Privilege)
# -----------------

# Creates the role that the Lambda service (running the Canary) assumes
resource "aws_iam_role" "canary_role" {
  name = "${local.project_name}-canary-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}

# Attaches the standard execution policy
resource "aws_iam_policy_attachment" "canary_exec_policy" {
  name       = "${local.project_name}-exec-attach"
  roles      = [aws_iam_role.canary_role.name]
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# -----------------
# 4. Synthetics Canary (Monitoring Check)
# -----------------

# Archiving the script code into a zip file for deployment
resource "archive_file" "canary_zip" {
  type        = "zip"
  source_content = local.canary_script_content
  output_path = "canary_script.zip"
}

# Canary resource: The active health checker
resource "aws_synthetics_canary" "portfolio_check" {
  name             = "${local.project_name}-canary"
  # S3 bucket must be created to store artifacts (logs, screenshots)
  artifact_s3_location = "s3://synthetics-canary-artifacts-${data.aws_caller_identity.current.account_id}-us-east-1/${local.project_name}"
  execution_role_arn = aws_iam_role.canary_role.arn
  handler          = "exports.handler" # The entry point function in the script
  runtime_version  = "SYNTHETICS_NODEJS_2_1"

  zip_file = filebase64(archive_file.
