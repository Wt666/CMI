# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACbd979f76fbcff11505f6b5a568eb9161']
auth_token = os.environ['81178896371d5a4c6d35e0b77183d6ac']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         messaging_service_sid='SMbb07878fbed1f987c7a22785427a1036',
         body='body',
         to='+18573361164'
     )

print(message.sid)