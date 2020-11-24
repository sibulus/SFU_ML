# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(649, 559)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.chooseInputLabel = QLabel(self.centralwidget)
        self.chooseInputLabel.setObjectName(u"chooseInputLabel")
        self.chooseInputLabel.setEnabled(True)

        self.gridLayout.addWidget(self.chooseInputLabel, 2, 0, 1, 1)

        self.inputLineEdit = QLineEdit(self.centralwidget)
        self.inputLineEdit.setObjectName(u"inputLineEdit")

        self.gridLayout.addWidget(self.inputLineEdit, 2, 1, 1, 2)

        self.chooseModelLabel = QLabel(self.centralwidget)
        self.chooseModelLabel.setObjectName(u"chooseModelLabel")

        self.gridLayout.addWidget(self.chooseModelLabel, 1, 0, 1, 1)

        self.chooseSerialPortLabel = QLabel(self.centralwidget)
        self.chooseSerialPortLabel.setObjectName(u"chooseSerialPortLabel")

        self.gridLayout.addWidget(self.chooseSerialPortLabel, 4, 0, 1, 1)

        self.chooseOutputFolderLabel = QLabel(self.centralwidget)
        self.chooseOutputFolderLabel.setObjectName(u"chooseOutputFolderLabel")

        self.gridLayout.addWidget(self.chooseOutputFolderLabel, 3, 0, 1, 1)

        self.chooseLabLabel = QLabel(self.centralwidget)
        self.chooseLabLabel.setObjectName(u"chooseLabLabel")

        self.gridLayout.addWidget(self.chooseLabLabel, 0, 0, 1, 1)

        self.browseInputButton = QPushButton(self.centralwidget)
        self.browseInputButton.setObjectName(u"browseInputButton")

        self.gridLayout.addWidget(self.browseInputButton, 2, 3, 1, 1)

        self.labNameComboBox = QComboBox(self.centralwidget)
        self.labNameComboBox.setObjectName(u"labNameComboBox")
        self.labNameComboBox.setEnabled(True)

        self.gridLayout.addWidget(self.labNameComboBox, 0, 1, 1, 3)

        self.serialPortComboBox = QComboBox(self.centralwidget)
        self.serialPortComboBox.setObjectName(u"serialPortComboBox")
        self.serialPortComboBox.setEnabled(True)

        self.gridLayout.addWidget(self.serialPortComboBox, 4, 1, 1, 1)

        self.connectDisconnectSerialButton = QPushButton(self.centralwidget)
        self.connectDisconnectSerialButton.setObjectName(u"connectDisconnectSerialButton")

        self.gridLayout.addWidget(self.connectDisconnectSerialButton, 4, 2, 1, 1)

        self.outputFolderLineEdit = QLineEdit(self.centralwidget)
        self.outputFolderLineEdit.setObjectName(u"outputFolderLineEdit")
        self.outputFolderLineEdit.setEnabled(True)

        self.gridLayout.addWidget(self.outputFolderLineEdit, 3, 1, 1, 2)

        self.browseOutputButton = QPushButton(self.centralwidget)
        self.browseOutputButton.setObjectName(u"browseOutputButton")

        self.gridLayout.addWidget(self.browseOutputButton, 3, 3, 1, 1)

        self.refreshSerialPortsButton = QPushButton(self.centralwidget)
        self.refreshSerialPortsButton.setObjectName(u"refreshSerialPortsButton")

        self.gridLayout.addWidget(self.refreshSerialPortsButton, 4, 3, 1, 1)

        self.modelLineEdit = QLineEdit(self.centralwidget)
        self.modelLineEdit.setObjectName(u"modelLineEdit")

        self.gridLayout.addWidget(self.modelLineEdit, 1, 1, 1, 1)

        self.useDefaultModelCheckbox = QCheckBox(self.centralwidget)
        self.useDefaultModelCheckbox.setObjectName(u"useDefaultModelCheckbox")

        self.gridLayout.addWidget(self.useDefaultModelCheckbox, 1, 2, 1, 1)

        self.browseModelButton = QPushButton(self.centralwidget)
        self.browseModelButton.setObjectName(u"browseModelButton")

        self.gridLayout.addWidget(self.browseModelButton, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.startStopButton = QPushButton(self.centralwidget)
        self.startStopButton.setObjectName(u"startStopButton")

        self.verticalLayout.addWidget(self.startStopButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.logSplitterMajor = QSplitter(self.centralwidget)
        self.logSplitterMajor.setObjectName(u"logSplitterMajor")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logSplitterMajor.sizePolicy().hasHeightForWidth())
        self.logSplitterMajor.setSizePolicy(sizePolicy)
        self.logSplitterMajor.setOrientation(Qt.Vertical)
        self.processingLogLabel = QLabel(self.logSplitterMajor)
        self.processingLogLabel.setObjectName(u"processingLogLabel")
        self.logSplitterMajor.addWidget(self.processingLogLabel)
        self.logSplitter = QSplitter(self.logSplitterMajor)
        self.logSplitter.setObjectName(u"logSplitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logSplitter.sizePolicy().hasHeightForWidth())
        self.logSplitter.setSizePolicy(sizePolicy1)
        self.logSplitter.setOrientation(Qt.Horizontal)
        self.logTextBrowser = QTextBrowser(self.logSplitter)
        self.logTextBrowser.setObjectName(u"logTextBrowser")
        self.logSplitter.addWidget(self.logTextBrowser)
        self.logButtonsSplitter = QSplitter(self.logSplitter)
        self.logButtonsSplitter.setObjectName(u"logButtonsSplitter")
        self.logButtonsSplitter.setOrientation(Qt.Vertical)
        self.clearLogButton = QPushButton(self.logButtonsSplitter)
        self.clearLogButton.setObjectName(u"clearLogButton")
        self.logButtonsSplitter.addWidget(self.clearLogButton)
        self.saveLogButton = QPushButton(self.logButtonsSplitter)
        self.saveLogButton.setObjectName(u"saveLogButton")
        self.logButtonsSplitter.addWidget(self.saveLogButton)
        self.logSplitter.addWidget(self.logButtonsSplitter)
        self.logSplitterMajor.addWidget(self.logSplitter)

        self.verticalLayout_2.addWidget(self.logSplitterMajor)

        self.progressLayout = QFormLayout()
        self.progressLayout.setObjectName(u"progressLayout")
        self.progressLabel = QLabel(self.centralwidget)
        self.progressLabel.setObjectName(u"progressLabel")

        self.progressLayout.setWidget(1, QFormLayout.LabelRole, self.progressLabel)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.progressLayout.setWidget(1, QFormLayout.FieldRole, self.progressBar)

        self.lastLogTextLabel = QLabel(self.centralwidget)
        self.lastLogTextLabel.setObjectName(u"lastLogTextLabel")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lastLogTextLabel.setFont(font)

        self.progressLayout.setWidget(0, QFormLayout.SpanningRole, self.lastLogTextLabel)


        self.verticalLayout_2.addLayout(self.progressLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 649, 26))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.chooseInputLabel.setBuddy(self.inputLineEdit)
        self.chooseSerialPortLabel.setBuddy(self.serialPortComboBox)
        self.chooseOutputFolderLabel.setBuddy(self.outputFolderLineEdit)
        self.chooseLabLabel.setBuddy(self.labNameComboBox)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.labNameComboBox, self.inputLineEdit)
        QWidget.setTabOrder(self.inputLineEdit, self.browseInputButton)
        QWidget.setTabOrder(self.browseInputButton, self.outputFolderLineEdit)
        QWidget.setTabOrder(self.outputFolderLineEdit, self.browseOutputButton)
        QWidget.setTabOrder(self.browseOutputButton, self.serialPortComboBox)
        QWidget.setTabOrder(self.serialPortComboBox, self.startStopButton)
        QWidget.setTabOrder(self.startStopButton, self.clearLogButton)
        QWidget.setTabOrder(self.clearLogButton, self.saveLogButton)
        QWidget.setTabOrder(self.saveLogButton, self.logTextBrowser)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.chooseInputLabel.setText(QCoreApplication.translate("MainWindow", u"Choose &Input CSV file", None))
        self.chooseModelLabel.setText(QCoreApplication.translate("MainWindow", u"Choose Model", None))
        self.chooseSerialPortLabel.setText(QCoreApplication.translate("MainWindow", u"Serial &Port", None))
        self.chooseOutputFolderLabel.setText(QCoreApplication.translate("MainWindow", u"Choose &Output Folder", None))
        self.chooseLabLabel.setText(QCoreApplication.translate("MainWindow", u"Choose &Lab", None))
        self.browseInputButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.connectDisconnectSerialButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.browseOutputButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.refreshSerialPortsButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.useDefaultModelCheckbox.setText(QCoreApplication.translate("MainWindow", u"Use Default Model", None))
        self.browseModelButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.startStopButton.setText(QCoreApplication.translate("MainWindow", u"Start Processing", None))
        self.processingLogLabel.setText(QCoreApplication.translate("MainWindow", u"Processing Log", None))
        self.clearLogButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.saveLogButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.progressLabel.setText(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.lastLogTextLabel.setText("")
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

