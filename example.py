import twilio
from twilio.rest import TwilioRestClient
import os
import csv
# linking to csv
num=open('Numbers.csv')
csvnum=csv.reader(num)

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.getenv('MY_ACCOUNT_SID')
auth_token  = os.getenv('MY_AUTH_TOKEN')
client = TwilioRestClient(account_sid, auth_token)
for row in csvnum:
	print row
	message = client.messages.create(body="Twilio working, buy a number",
    	to=row,    # Replace with your phone number or text me if you really want to
    	from_="+15005550006") # Replace with your Twilio number
	print message.sid
