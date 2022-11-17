# import twilio
from twilio.rest import Client
import os
# Your Account SID from twilio.com/console
account_sid = "ACbd979f76fbcff11505f6b5a568eb9161"
# Your Auth Token from twilio.com/console
auth_token  = "81178896371d5a4c6d35e0b77183d6ac"

client = Client(account_sid, auth_token)

# message = client.messages.create(
#     to="+85267657478",
#     from_="+18573361164",
#     body="Join Earth's mightiest heroes. Like Kevin Bacon.")

# call=client.calls.get("SM6c5fdf31dcf57dda867582bc316d13e2")
# print(message.sid)
# print(call.to)
for sms in client.messages.list():
  print(sms.to)

# from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['ACbd979f76fbcff11505f6b5a568eb9161']
# auth_token = os.environ['81178896371d5a4c6d35e0b77183d6ac']
# client = Client(account_sid, auth_token)
#
# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+18573361164',
#                      to='+85267657478'
#                  )

# print(message.sid)