import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtUiTools import QUiLoader #to load UI directly
from PySide2.QtCore import QFile, QIODevice

import os

def initMainWindow(window):
    window.setWindowTitle("Lab Tools v1.0 - Applications of ML in Mechatronics")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "mainwindow.ui"

    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
        sys.exit(-1)
    loader = QUiLoader()
    mainWindow = loader.load(ui_file)
    initMainWindow(mainWindow)
    ui_file.close()
    if not mainWindow:
        print(loader.errorString())
        sys.exit(-1)

    mainWindow.show()
    sys.exit(app.exec_())
