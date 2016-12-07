from config import Twilio

from twilio.rest import TwilioRestClient

def textmyself(message):
    twilioCli = TwilioRestClient(TwilioConfig.ACCOUNT_SID, TwilioConfig.AUTH_TOKEN)
    twilioCli.messages.create(body=message, from_=TwilioConfig.TWILIO_NUMBER, to=TwillioConfig.MY_NUMBER)

if __name__ == "__main__":
    textmyself('km viettel 100% vao ngay mai')
