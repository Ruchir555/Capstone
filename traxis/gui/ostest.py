from os import listdir
from os import getcwd
from os.path import isfile, join
# from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore


mypath = getcwd()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print("hi",mypath)
# print("onlyfiles", onlyfiles)


print(QtCore.QDir.currentPath())
print(getcwd())

for i in getcwd():
    print(i)