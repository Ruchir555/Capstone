from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *


fileName = QtWidgets.QFileDialog.getOpenFileName(
            None, "Load Session", QtCore.QDir.currentPath(),
            "HEP Track Analysis (*.json);;All Files (*)")

print(fileName)