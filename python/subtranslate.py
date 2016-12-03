import translate

class SubtitleTranslate:
    def __init__(self, translate):
        self.translate = translate

    def parseSub(self, filename):
        f = open(filename, "r")
        data = f.read()
        result = [
            {
                "order" : sub.split("\n")[0],
                "time" : sub.split("\n")[1],
                "text" : sub.split("\n")[2:]
            }
        for sub in data.replace("\r", "").split("\n\n") if len(sub.split("\n")) > 2]
        return result

    def translateSub(self, data, _from="en", to="vi"):
        translateData = data[:]
        for i in range(len(translateData)):
            for j in range(len(translateData[i]["text"])):
                print translateData[i]["text"][j]
                translateText = t.bing(translateData[i]["text"][j], _from=_from, to=to)
                translateData[i]["text"][j] = translateText
        return translateData

    def writeSub(self, filename, data):
        f = open(filename, "wb")
        for i in range(len(data)):
            try:
                f.write(data[i]["order"].encode("utf-8") + "\n")
                f.write(data[i]["time"].encode("utf-8") + "\n") 
                for j in range(len(data[i]["text"])):
                    f.write(data[i]["text"][j].encode("utf-8") + "\n")
                    f.write("\n")
            except:
                pass

if __name__ == "__main__":
    t = translate.Translate()
    s = SubtitleTranslate(t)
    sub_data = s.parseSub("Shooter.S01E03.HDTV.x264-FLEET.srt")
    translate_data = s.translateSub(sub_data)
    s.writeSub(r"content/sub.txt", sub_data)
