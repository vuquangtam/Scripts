from PyQt4.QtCore import (QTime, QTimer, Qt, SIGNAL, QObject)
from PyQt4.QtGui import (QApplication, QLabel, QFont)
from pymouse import PyMouseEvent
import subprocess
import sys
import threading
from textblob import TextBlob

def getSelection():
    selection = subprocess.check_output(["xsel"])
    return selection

def translate(text, language):
    print text
    try:
        text = TextBlob(text)
        result = text.translate(to=language)
        return result.string
    except:
        return "Error"

def notify(text, kind=""):
    if kind == "notification":
        subprocess.call(["notify-send", text])
    else:
        subprocess.call(["zenity", "--info", "--title='Translate'", "--text", text])

class Clicktranslate(PyMouseEvent, QObject):
    def __init__(self):
        PyMouseEvent.__init__(self)
        QObject.__init__(self)
        self.oldSel = ""
        
    def click(self, x, y, button, press):
        print self.oldSel
        if button == 1:
            text = getSelection()
            #print text
            if text and text != self.oldSel:
                self.oldSel = text
                result = translate(text, "vi")
                #print result
                self.emit(SIGNAL("translate"), (text + "<br>--------------<br>" + result, (x, y)))
                #self.showLabel(text + "\n" +result)
                #notify(text + "\n" + str(result))
        else:  # Exit if any other mouse button used
            self.stop()

class App(QApplication):
    def __init__(self, *args):
        QApplication.__init__(self, *args)
        self.translate = Clicktranslate()
        
        self.messageStyle = "<font color=green size=3><b>%s</b></font>"
        self.label = QLabel()
        self.label.setWordWrap(True);
        self.label.setWindowFlags(Qt.ToolTip)
        self.label.mousePressEvent = self.hideLabel
        self.connect(self.translate, SIGNAL("translate"), self.showLabel)
        
    def showLabel(self, data=("Translate...",(300, 300))):
        self.label.setText(self.messageStyle % data[0])
        self.label.adjustSize()
        self.label.move(*data[1])
        self.label.show() 

    def hideLabel(self, *args):
        self.label.hide()
        
    def exec_(self):
        threading.Thread(target=self.translate.run).start()
        QApplication.exec_()

app = App(sys.argv)
app.exec_()