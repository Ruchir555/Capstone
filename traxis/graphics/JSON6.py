import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout, QListWidget, QMessageBox
from PyQt5.QtWidgets import *
from os import listdir
from os import getcwd
from os.path import isfile, join

class JSONClass(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI(getcwd())

    def initUI(self, dir):
        vbox = QVBoxLayout(self)
        # self.buildList(dir)
        AllFilesList = [f for f in listdir(dir) if isfile(join(dir, f))]
        JSONFileList = []

        for j in range(0, len(AllFilesList)):
            if (AllFilesList[j][-1] == 'n') and (AllFilesList[j][-2] == 'o') and (AllFilesList[j][-3] == 's') and (AllFilesList[j][-4] == 'j') and (AllFilesList[j][-5] == '.'):
                JSONFileList.append(AllFilesList[j])

        for i in range(0, len(JSONFileList)):
            # currentItem = self.addListItem(self, dir, JSONFileList[i])
            # QListWidget().addItem(currentItem.name)
            QListWidget().addItem(JSONFileList[i])

        vbox.addWidget(QListWidget())
        self.setLayout(vbox)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QListWidget')
        self.show()


    # def buildList(self, dir):
    #     AllFilesList = [f for f in listdir(dir) if isfile(join(dir, f))]
    #     JSONFileList = []
    #     for j in range(0, len(AllFilesList)):
    #         if (AllFilesList[j][-1] == 'n') and (AllFilesList[j][-2] == 'o') and (AllFilesList[j][-3] == 's') and (
    #                 AllFilesList[j][-4] == 'j') and (AllFilesList[j][-5] == '.'):
    #             JSONFileList.append(AllFilesList[j])
    #
    #     for i in range(0, len(JSONFileList)):
    #         currentItem = self.addListItem(self, dir, JSONFileList[i])
    #         QListWidget().addItem(currentItem.name)

    def addListItem(self, dir, file_name):
        newItem = JSONitem(self, dir, file_name)
        return newItem

    def onClicked(self, item):
        QMessageBox.information(self, "Info", item.text())


class JSONitem(QListWidgetItem):

    def __init__(self, dir_loc, FileName, parent=None):
        # Directory of JSON file
        self.loc = dir_loc

        # Name of JSON file
        self.name = FileName
        # markerName = "Point {}".format(self.id)

        # call the __init__ method of the QListWidgetItem superclass, passing
        # the file's name and the marker's parent widget.
        super().__init__(FileName, parent)



