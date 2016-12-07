import requests
import subprocess
import urllib
import bs4
def getSelection():
    selection = subprocess.check_output(["xsel"])
    return selection

class translateGoogle:

    def __init__(self, _from, _to):
        self._from = _from
        self._to = _to
        self.url = self.getUrl(_from, _to)
        
    def getUrl(self, _from, _to):
        return "https://translate.google.com/#%s/%s/" % (_from, _to)

    def translate(self, text):
        #text = urllib.urlencode(text)
        req = requests.get(self.url + text)
        print self.url + text
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text, "lxml")
        result = soup.select("span#result_box span")
        print result

if __name__ == "__main__":
    translate = translateGoogle("en", "vi")
    translate.translate("close")
    