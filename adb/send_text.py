import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

import time 

client = WebClient(token='xoxb-878537608886-1683457705654-Vx4DSD1U2yGuIc2GCxmpVwhI')

def send_message_to_slack(content):

    try:
        response = client.chat_postMessage(channel='梦幻', text=content)
        # assert response["message"]["text"] == "Hello world!"
        # print(response)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")
        
    time.sleep(10)    
        
        
# print('test')        
# send_message_to_slack('111233哈哈')


