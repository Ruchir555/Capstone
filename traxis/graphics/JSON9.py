import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout, QListWidget, QMessageBox
from PyQt5.QtWidgets import *
from os import listdir
from os import getcwd
from os.path import isfile, join, normpath


class Example(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI(getcwd())

    def initUI(self, path):

        vbox = QVBoxLayout()    #self
        self.listWidget = QListWidget()
        self.listWidget.itemDoubleClicked.connect(self.onClicked)
        vbox.addWidget(self.listWidget)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 300)
        # self.setMinimumWidth(100)
        self.setWindowTitle('QListWidget')
        self.show()
        self.append_text(path)


    def onClicked(self, item):
        QMessageBox.information(self, "Info", item.text())

    def append_text(self, path):
        dir = path
        # listWidget = QListWidget()
        self.listWidget.clear()
        AllFilesList = [f for f in listdir(dir) if isfile(join(dir, f))]
        JSONFileList = []

        for j in range(0, len(AllFilesList)):
            if (AllFilesList[j][-1] == 'n') and (AllFilesList[j][-2] == 'o') and (AllFilesList[j][-3] == 's') and (AllFilesList[j][-4] == 'j') and (AllFilesList[j][-5] == '.'):
                JSONFileList.append(AllFilesList[j])

        for i in range(0, len(JSONFileList)):
            self.listWidget.addItem(JSONFileList[i])
            # print(JSONFileList[i])
