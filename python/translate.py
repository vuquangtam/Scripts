import requests
import json
import urllib
import secret

class Translate:
    def translate(self, text, to="vi"):
        url = "http://www.transltr.org/api/translate?text="+ text + "&to=" + to
        req = requests.get(url)

        try:
            result = json.loads(req.text)["translationText"]
        except:
            result = ""

        return result
    
    def bing(self, text, _from="en", to="vi", bing_id=secret.BING_ID, bing_secret=secret.BING_SECRET):
        args = {
            'client_id': bing_id, #your client id here
            'client_secret': bing_secret, #your azure secret here
            'scope': 'http://api.microsofttranslator.com',
            'grant_type': 'client_credentials'
        }
        oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
        oauth_junk = json.loads(requests.post(oauth_url,data=urllib.urlencode(args)).content)
        translation_args = {
            'text': text,
            'to': to,
            'from': _from
        }
        headers={'Authorization': 'Bearer '+oauth_junk['access_token']}
        translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
        translation_result = requests.get(translation_url+urllib.urlencode(translation_args),headers=headers)
        return translation_result.text.replace('"', "")


if __name__ == "__main__":
    text = "but my wife and daughter are left alone."
    t = Translate()
    print t.translate(text)
    print t.bing(text)
