import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token='xoxb-878537608886-1683457705654-gfES9lJ8jYgOhOp4nAx4K7Ac')

def send_pic_to_slack():

    try:
        filepath="./home.jpg"
        response = client.files_upload(channels='梦幻', file=filepath)

        assert response["file"]  # the uploaded file
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")