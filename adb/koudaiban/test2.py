


import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

bot_token = 'xoxb-878537608886-1694511546722-izEl5QrcB353Fk5tEQ6RgQjQ'

app_token='xapp-1-A01LT4177KK-1691430861685-afad308087194061b8dcd5c4378f18e084fcfd462562a6467a92bd2f9e787c31'

# Install the Slack app and get xoxb- token in advance
app = App(token=bot_token)

print(app)

@app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")

@app.event("app_mention")
def event_test(say):
    say("Hi there!")
    
# This will match any message that contains 👋
@app.message(":wave:")
def say_hello(message, say):
    user = message['user']
    say(f"Hi there, <@{user}>!")
    
# Listens for messages containing "knock knock" and responds with an italicized "who's there?"
@app.message("knock knock")
def ask_who(message, say):
    say("_Who's there?_")


if __name__ == "__main__":
    SocketModeHandler(app, app_token).start()