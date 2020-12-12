###########################################################
from PyQt5 import QtWidgets, QtCore
###########################################################
from PyQt5.QtWidgets import QVBoxLayout, QListWidget, QMessageBox
from PyQt5.QtWidgets import *
from os import listdir
from os import getcwd
from os.path import isfile, join
import json


class Example(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.cd = getcwd()
        self.initUI(self.cd)

    def initUI(self, path):
        vbox = QVBoxLayout()
        self.listWidget = QListWidget()
        ###########################################################
        # self.listWidget.itemDoubleClicked.connect(self.onClicked)
        ###########################################################
        vbox.addWidget(self.listWidget)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('QListWidget')
        self.show()
        self.append_text(path)

    def append_text(self, path):
        self.cd = path
        # print("Self.cd:", self.cd)
        self.listWidget.clear()
        AllFilesList = [f for f in listdir(self.cd ) if isfile(join(self.cd , f))]
        JSONFileList = []

        for j in range(0, len(AllFilesList)):
            if (AllFilesList[j][-1] == 'n') and (AllFilesList[j][-2] == 'o') and (AllFilesList[j][-3] == 's') and (AllFilesList[j][-4] == 'j') and (AllFilesList[j][-5] == '.'):
                JSONFileList.append(AllFilesList[j])

        for i in range(0, len(JSONFileList)):
            self.listWidget.addItem(JSONFileList[i])

    def loadJSON(self, item):

        fileName = self.cd + '\\' + item.text()
        print('filename:', fileName)

        # return if no file was selected
        if not fileName:
            return

        else:
            # open the file contents
            with open(fileName, 'r') as loadFile:
                # try to load the file contents as a JSON formatted object
                try:
                    loadData = json.load(loadFile)
                except:
                    self.displayMessage("NOTICE: Invalid JSON file: {}".format(
                        fileName))
                    return

                # get the image filename from the saved session data
                imageFileName = loadData.get('imageFileName')

                # if the image filename is missing, return
                if not imageFileName:
                    self.displayMessage("NOTICE: No image file name found in saved session data: {}".format(fileName))
                    return

                # try to open the image. If it fails to open, return
                print("Image file name", imageFileName)
                print('ERROR')
                opened = self.openImage(imageFileName)
                if not opened:
                    return

                # get the track marker data from the saved session
                points = loadData.get('points')
                if points:
                    # add each track marker to the marker list
                    for point in points:
                        pointDesignation = point["designation"]
                        x = point['x']
                        y = point['y']
                        addedMarker = self.markerList.addMarker(
                            x, y, self.pointSize,
                            self.lineWidth, self.scene)
                        # set the appropriate designation for each marker
                        addedMarker.setDesignation(pointDesignation)

                # get the dl data from the saved session
                dl = loadData.get('dl')
                # if it is a float, set it to the dl text box value
                try:
                    float(dl)
                    self.dlLineEdit.setText(dl)
                except (ValueError, TypeError):
                    pass

                # get the data for the initial and final points for the
                # reference line
                refInitialPoint = loadData.get('refInitialPoint')
                refFinalPoint = loadData.get('refFinalPoint')
                if refInitialPoint and refFinalPoint:
                    # set the initial point, line and final point of the
                    # reference line
                    self.angleRefLine.setInitialPoint(
                        refInitialPoint['x'], refInitialPoint['y'],
                        self.pointSize, self.lineWidth, self.scene)
                    self.angleRefLine.drawLine(
                        refFinalPoint['x'], refFinalPoint['y'],
                        self.lineWidth, self.scene)
                    self.angleRefLine.setFinalPoint(
                        refFinalPoint['x'], refFinalPoint['y'],
                        self.pointSize, self.lineWidth, self.scene)


    def onClicked(self, item):
        QMessageBox.information(self, "Info", item.text())
        # self.loadJSON(item)
        # maingui.printer(self)




