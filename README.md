# Daily AI News Agent

## Overview

Daily AI News Agent is an AI-powered serverless application built using AWS. The agent automatically runs every day at 8:00 AM (Asia/Colombo), collects the latest AI and technology news using Amazon Bedrock Nova Lite, and sends the news directly to the user's email using Amazon SES.

This project was created for the AWS Builder Center Weekend Agent Challenge.

---

## Features

- Automatically runs every day at 8:00 AM
- Uses Amazon Bedrock Nova Lite to generate AI news
- Sends AI-generated news via Amazon SES
- Fully serverless architecture
- No manual intervention required

---

## AWS Services Used

- Amazon Bedrock (Nova Lite)
- AWS Lambda
- Amazon EventBridge Scheduler
- Amazon Simple Email Service (SES)
- AWS IAM

---

## Architecture

EventBridge Scheduler
        
        ↓
AWS Lambda
       
        ↓
Amazon Bedrock (Nova Lite)
       
        ↓
Generate Daily AI News
       
        ↓
Amazon SES
       
        ↓
Gmail Inbox

---

## Project Files

- lambda_function.py
- README.md

---

## How It Works

1. EventBridge Scheduler triggers the Lambda function every day at 8:00 AM.
2. Lambda sends a prompt to Amazon Bedrock Nova Lite.
3. Bedrock generates the latest AI and technology news.
4. Lambda sends the generated news to Amazon SES.
5. Amazon SES delivers the email to the configured Gmail address.

---

## Learning Outcomes

During this project I learned how to:

- Build serverless AI applications
- Use Amazon Bedrock foundation models
- Schedule automatic jobs using EventBridge Scheduler
- Send emails using Amazon SES
- Deploy and test AWS Lambda functions
- Configure IAM permissions

---

## Author

**Mohammed Jumail**

AWS Builder Center Weekend Challenge 2026
