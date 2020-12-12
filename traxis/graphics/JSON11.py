from PyQt5.QtWidgets import QVBoxLayout, QListWidget, QMessageBox
from PyQt5.QtWidgets import *
from os import listdir
from os import getcwd
from os.path import isfile, join

class Example(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cd = getcwd()
        self.initUI(self.cd)

    def initUI(self, path):
        vbox = QVBoxLayout()
        self.listWidget = QListWidget()
        vbox.addWidget(self.listWidget)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('QListWidget')
        self.show()
        self.append_text(path)

    def append_text(self, path):
        self.cd = path
        self.listWidget.clear()
        AllFilesList = [f for f in listdir(self.cd ) if isfile(join(self.cd , f))]
        JSONFileList = []

        for j in range(0, len(AllFilesList)):
            if (AllFilesList[j][-1] == 'n') and (AllFilesList[j][-2] == 'o') and (AllFilesList[j][-3] == 's') and (AllFilesList[j][-4] == 'j') and (AllFilesList[j][-5] == '.'):
                JSONFileList.append(AllFilesList[j])

        for i in range(0, len(JSONFileList)):
            self.listWidget.addItem(JSONFileList[i])
