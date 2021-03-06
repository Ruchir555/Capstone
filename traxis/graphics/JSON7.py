import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout, QListWidget, QMessageBox
from PyQt5.QtWidgets import *
from os import listdir
from os import getcwd
from os.path import isfile, join



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        dir = getcwd()
        vbox = QVBoxLayout(self)
        listWidget = QListWidget()
        AllFilesList = [f for f in listdir(dir) if isfile(join(dir, f))]
        JSONFileList = []

        for j in range(0, len(AllFilesList)):
            if (AllFilesList[j][-1] == 'n') and (AllFilesList[j][-2] == 'o') and (AllFilesList[j][-3] == 's') and (
                    AllFilesList[j][-4] == 'j') and (AllFilesList[j][-5] == '.'):
                JSONFileList.append(AllFilesList[j])

        for i in range(0, len(JSONFileList)):
            # currentItem = self.addListItem(self, dir, JSONFileList[i])
            # QListWidget().addItem(currentItem.name)
            listWidget.addItem(JSONFileList[i])

        listWidget.itemDoubleClicked.connect(self.onClicked)

        vbox.addWidget(listWidget)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QListWidget')
        self.show()

    def onClicked(self, item):
        QMessageBox.information(self, "Info", item.text())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()