"""
The Main App factory (Slack in main thread; Discord in its own thread)
"""
import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from keep_alive import keep_alive

load_dotenv()

# 1) SLACK
slack_bot = App(token=os.environ["SLACK_BOT_TOKEN"])

@slack_bot.event("app_mention")
def on_message_slack(body, say):
    """
    [Slack]
    
    When the bot is mentioned, strip off the mention tag and pass
    the clean text to `chatting(...)`, then reply with its response.
    """

    event = body["event"]
    full_text = event["text"]
    bot_id = body["authorizations"][0]["user_id"]

    if bot_id in full_text:
        response = 'Hey'

        # the bot returns the response from the LLM
        say(response)

def start_slack_socket_mode():
    """
    [Slack] this must run in the main thread (so signal handlers can be registered).
    """
    # Check documentation for Slack's Socket Mode -- https://api.slack.com/apis/socket-mode
    handler = SocketModeHandler(slack_bot, os.environ["SLACK_APP_TOKEN"])
    handler.start()



if __name__ == "__main__":
    keep_alive()

    start_slack_socket_mode()
