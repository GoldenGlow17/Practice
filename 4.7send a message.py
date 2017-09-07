from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC82b362a46e70f57c258e4c4ab468ece4"
# Your Auth Token from twilio.com/console
auth_token  = "83b7857d32e6c6f1e43"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8617370442256",   # Replace with your phone number
    from_="+3197014200321",# Replace with your Twilio number
    body="How are you today?")

print(message.sid)