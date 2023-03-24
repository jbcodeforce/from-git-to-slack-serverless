import json, os, requests
import base64

def send_slack_message(payload):
    """Send a Slack message to a channel via a webhook. 
    
    Args:
        payload (dict): Dictionary containing Slack message, i.e. {"text": "This is a test"}
    
    Returns:
        HTTP response code, i.e. <Response [503]>
    """
    webhook = os.environ.get("SLACK_WEBHOOK")
    return requests.post(webhook, json.dumps(payload))
    
def lambda_handler(event, context):
    """Lambda function

    Parameters
    ----------
    event: dict, required
        Git Event

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    
    # print(event)
    #bodyEncoded = event["body"]
    #bodyDecoded = base64.b64decode(bodyEncoded).decode('UTF-8')
    body=json.loads(event["body"])
    print(body)
    repo = body["repository"]["name"]
    stars = body["repository"]["stargazers_count"]
    message = { "attachments": [{}] }
    message["attachments"][0]["pretext"] = "There is a new Github star for " + repo + " repo!"
    message["attachments"][0]["text"] = repo + " now has " + str(stars) + " stars!" + "\nYour new :star: was made by ."
    message["attachments"][0]["footer"] = "Serverless App"
    message["attachments"][0]["footer_icon"] = "https://platform.slack-edge.com/img/default_application_icon.png"

    send_slack_message(message)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Done",
        }),
    }
