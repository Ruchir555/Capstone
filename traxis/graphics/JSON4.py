import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout, QListWidget
from PyQt5.QtWidgets import *
from os import listdir
from os import getcwd
from os.path import isfile, join

class JSONClass(QListWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.buildList(getcwd())
        
    def buildList(self, dir):
        AllFilesList = [f for f in listdir(dir) if isfile(join(dir, f))]
        JSONFileList = []
        for j in range(0, len(AllFilesList)):
            if (AllFilesList[j][-1] == 'n') and (AllFilesList[j][-2] == 'o') and (AllFilesList[j][-3] == 's') and (AllFilesList[j][-4] == 'j') and (AllFilesList[j][-5] == '.'):
                JSONFileList.append(AllFilesList[j])

        for i in range(0, len(JSONFileList)):
            self.addListItem(self, dir, JSONFileList[i])

    def addListItem(self, dir, file_name):
        newItem = JSONitem(self, dir, file_name)
        return newItem





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



