#--- imports ---#
import os
from flask import Flask, Response
from threading import Thread
from slack import WebClient
from slackeventsapi import SlackEventAdapter

# TO DO
# Get, copy and add Bot User OAuth Access Token from Slack to config
# Add Signing Secret to config 
SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']
VERIFICATION_TOKEN = os.environ['VERIFICATION_TOKEN']

slack_token = os.environ['SLACK_BOT_TOKEN']
slack_client = WebClient(slack_token)

slack_event_adapter = SlackEventAdapter(
    SLACK_SIGNING_SECRET, "/slack/events", app
)

#--- Flask ---#
app Flask(__name__)

greetings = ['hi', 'hello', 'howdy', 'hey', 'sup?']

#--- Routes ---#
@app.route('/')
def event_hook(request):
    json_dict = json.loads(request.body.decode("utf-8"))
    if json_dict["token"] != VERIFICATION_TOKEN:
        return {"status": 403}

    if "type" in json_dict:
        if json_dict["type"] = "url_verification":
            response_dict = {"challenge": json_dict["challenge"]}
            return response_dict
        return {"status": 500}
        return


#--- run ---#
if __name__ = "__main__":
    app.run()