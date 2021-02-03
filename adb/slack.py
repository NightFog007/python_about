import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token='xxxx')

try:
    response = client.chat_postMessage(channel='梦幻', text="Hello world22!")
    assert response["message"]["text"] == "Hello world!"
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")