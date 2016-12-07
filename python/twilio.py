#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

# Preset values:
from config import Twilio

from twilio.rest import TwilioRestClient

def textmyself(message):
	twilioCli = TwilioRestClient(TwilioConfig.ACCOUNT_SID, TwilioConfig.AUTH_TOKEN)
	twilioCli.messages.create(body=message, from_=TwilioConfig.TWILIO_NUMBER, to=TwillioConfig.MY_NUMBER)

textmyself('km viettel 100% vao ngay mai')
