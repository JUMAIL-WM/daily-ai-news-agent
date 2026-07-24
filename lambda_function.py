import json
import boto3
from datetime import datetime

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
ses = boto3.client("ses", region_name="us-east-1")

SENDER = "jumailwm@gmail.com"
RECIPIENT = "jumailwm@gmail.com"

PROMPT = """
Give me today's top 5 technology and AI news.

For each news item include:
- Title
- 2-3 sentence summary
- Why it matters

Return the result in plain text.
"""

def get_ai_news():

    request = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": PROMPT
                    }
                ]
            }
        ]
    }

    response = bedrock.invoke_model(
        modelId="amazon.nova-lite-v1:0",
        body=json.dumps(request),
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(response["body"].read())

    return result["output"]["message"]["content"][0]["text"]


def send_email(news):

    today = datetime.now().strftime("%d %B %Y")

    ses.send_email(
        Source=SENDER,
        Destination={
            "ToAddresses": [RECIPIENT]
        },
        Message={
            "Subject": {
                "Data": f"Daily AI News - {today}"
            },
            "Body": {
                "Text": {
                    "Data": news
                }
            }
        }
    )


def lambda_handler(event, context):

    try:

        news = get_ai_news()

        send_email(news)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Email sent successfully",
                "news": news
            })
        }

    except Exception as e:

        return {
            "statusCode": 500,
            "body": json.dumps(str(e))
        }
