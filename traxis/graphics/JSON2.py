import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import *
from os import listdir
from os import getcwd
from os.path import isfile, join
# import maingui


mypath = getcwd()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
FileList = []

for j in range(0, len(onlyfiles)):
    if (onlyfiles[j][-1] =='n') and (onlyfiles[j][-2] =='o') and (onlyfiles[j][-3] =='s') and (onlyfiles[j][-4] =='j') and (onlyfiles[j][-4] =='.'):
        FileList.append(onlyfiles[j])


class JSONClass(QListWidget):         #QWidget

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()


    def initUI(self):

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tb, 1)

        self.setLayout(vbox)

        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 300)
        self.show()


        self.append_text()

    def append_text(self):

        # allText = ['a', 'b', 'c', 'd', 'e']

        allText = FileList

        for i in range(0, len(allText)):
            text = allText[i]
            self.tb.append(text)


