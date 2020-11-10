# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/converter.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(816, 338)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(20, 260, 361, 28))
        self.exitButton.setObjectName("exitButton")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(410, 260, 391, 28))
        self.resetButton.setObjectName("resetButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 50, 781, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(20, 300, 55, 16))
        self.statusLabel.setObjectName("statusLabel")
        self.liveDatenBox = QtWidgets.QCheckBox(self.centralwidget)
        self.liveDatenBox.setGeometry(QtCore.QRect(710, 10, 91, 31))
        self.liveDatenBox.setObjectName("liveDatenBox")
        self.umrechnenButton = QtWidgets.QPushButton(self.centralwidget)
        self.umrechnenButton.setGeometry(QtCore.QRect(600, 10, 93, 28))
        self.umrechnenButton.setObjectName("umrechnenButton")
        self.waehrungLabel = QtWidgets.QLabel(self.centralwidget)
        self.waehrungLabel.setGeometry(QtCore.QRect(190, 20, 55, 16))
        self.waehrungLabel.setObjectName("waehrungLabel")
        self.zielInput = QtWidgets.QLineEdit(self.centralwidget)
        self.zielInput.setGeometry(QtCore.QRect(470, 20, 113, 22))
        self.zielInput.setObjectName("zielInput")
        self.zielLabel = QtWidgets.QLabel(self.centralwidget)
        self.zielLabel.setGeometry(QtCore.QRect(380, 20, 101, 16))
        self.zielLabel.setObjectName("zielLabel")
        self.waehrungInput = QtWidgets.QLineEdit(self.centralwidget)
        self.waehrungInput.setGeometry(QtCore.QRect(250, 20, 113, 22))
        self.waehrungInput.setObjectName("waehrungInput")
        self.betragLabel = QtWidgets.QLabel(self.centralwidget)
        self.betragLabel.setGeometry(QtCore.QRect(20, 20, 55, 16))
        self.betragLabel.setObjectName("betragLabel")
        self.betragInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.betragInput.setGeometry(QtCore.QRect(80, 20, 91, 22))
        self.betragInput.setObjectName("betragInput")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Currency Converter"))
        self.exitButton.setText(_translate("mainWindow", "Exit"))
        self.resetButton.setText(_translate("mainWindow", "Zurücksetzen"))
        self.statusLabel.setText(_translate("mainWindow", "Status:"))
        self.liveDatenBox.setText(_translate("mainWindow", "Live-Daten"))
        self.umrechnenButton.setText(_translate("mainWindow", "Umrechnen"))
        self.waehrungLabel.setText(_translate("mainWindow", "Währung:"))
        self.zielLabel.setText(_translate("mainWindow", "Zielwährungen:"))
        self.betragLabel.setText(_translate("mainWindow", "Betrag:"))
