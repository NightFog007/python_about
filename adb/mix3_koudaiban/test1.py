import os
from slack_sdk.web import WebClient
from slack_sdk.socket_mode import SocketModeClient

bot_token = 'xoxb-878537608886-1694511546722-izEl5QrcB353Fk5tEQ6RgQjQ'

app_token='xapp-1-A01LT4177KK-1691430861685-afad308087194061b8dcd5c4378f18e084fcfd462562a6467a92bd2f9e787c31'

# Initialize SocketModeClient with an app-level token + WebClient
client = SocketModeClient(
    # This app-level token will be used only for establishing a connection
    app_token=app_token,  # xapp-A111-222-xyz
    # You will be using this WebClient for performing Web API calls in listeners
    web_client=WebClient(token=bot_token)  # xoxb-111-222-xyz
)

from slack_sdk.socket_mode.response import SocketModeResponse
from slack_sdk.socket_mode.request import SocketModeRequest

def process(client: SocketModeClient, req: SocketModeRequest):
    if req.type == "events_api":
        # Acknowledge the request anyway
        response = SocketModeResponse(envelope_id=req.envelope_id)
        client.send_socket_mode_response(response)

        # Add a reaction to the message if it's a new message
        if req.payload["event"]["type"] == "message" \
            and req.payload["event"].get("subtype") is None:
            client.web_client.reactions_add(
                name="eyes",
                channel=req.payload["event"]["channel"],
                timestamp=req.payload["event"]["ts"],
            )

# Add a new listener to receive messages from Slack
# You can add more listeners like this
client.socket_mode_request_listeners.append(process)
# Establish a WebSocket connection to the Socket Mode servers
client.connect()
# Just not to stop this process
from threading import Event
Event().wait()