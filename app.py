'''
placeholder
'''
import os
from flask import Flask, request
import requests

app = Flask(__name__)

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")

@app.route("/slack/events", methods=["POST"])
def slack_events():
    '''
    placeholder
    '''
    data = request.json
    if "challenge" in data:
        return data["challenge"]  # For Slack verification

    if "event" in data:
        event = data["event"]
        if event.get("type") == "app_mention":
            user = event["user"]
            channel = event["channel"]
            message = f"Hello <@{user}>! 👋"

            requests.post("https://slack.com/api/chat.postMessage", {
                "token": SLACK_BOT_TOKEN,
                "channel": channel,
                "text": message
            }, headers={"Authorization": f"Bearer {SLACK_BOT_TOKEN}"})

    return "", 200
