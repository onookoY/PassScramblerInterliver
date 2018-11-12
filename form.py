# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(402, 490)
        self.lblMessage = QtWidgets.QLabel(Form)
        self.lblMessage.setGeometry(QtCore.QRect(9, 9, 60, 17))
        self.lblMessage.setObjectName("lblMessage")
        self.txteditMessage = QtWidgets.QTextEdit(Form)
        self.txteditMessage.setGeometry(QtCore.QRect(9, 32, 383, 31))
        self.txteditMessage.setObjectName("txteditMessage")
        self.btnGo = QtWidgets.QPushButton(Form)
        self.btnGo.setGeometry(QtCore.QRect(110, 70, 80, 25))
        self.btnGo.setObjectName("btnGo")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 100, 383, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lblCrc = QtWidgets.QLabel(Form)
        self.lblCrc.setGeometry(QtCore.QRect(10, 110, 81, 17))
        self.lblCrc.setObjectName("lblCrc")
        self.txteditCrc = QtWidgets.QTextEdit(Form)
        self.txteditCrc.setGeometry(QtCore.QRect(10, 130, 383, 31))
        self.txteditCrc.setObjectName("txteditCrc")
        self.lblScrambler = QtWidgets.QLabel(Form)
        self.lblScrambler.setGeometry(QtCore.QRect(10, 170, 63, 17))
        self.lblScrambler.setObjectName("lblScrambler")
        self.txteditScr = QtWidgets.QTextEdit(Form)
        self.txteditScr.setGeometry(QtCore.QRect(10, 190, 383, 31))
        self.txteditScr.setObjectName("txteditScr")
        self.lblInter = QtWidgets.QLabel(Form)
        self.lblInter.setGeometry(QtCore.QRect(10, 230, 62, 17))
        self.lblInter.setObjectName("lblInter")
        self.txteditInter = QtWidgets.QTextEdit(Form)
        self.txteditInter.setGeometry(QtCore.QRect(10, 250, 383, 31))
        self.txteditInter.setObjectName("txteditInter")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 290, 383, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lblDeint = QtWidgets.QLabel(Form)
        self.lblDeint.setGeometry(QtCore.QRect(10, 310, 81, 17))
        self.lblDeint.setObjectName("lblDeint")
        self.txteditDeint = QtWidgets.QTextEdit(Form)
        self.txteditDeint.setGeometry(QtCore.QRect(10, 330, 383, 31))
        self.txteditDeint.setObjectName("txteditDeint")
        self.lblDescr = QtWidgets.QLabel(Form)
        self.lblDescr.setGeometry(QtCore.QRect(10, 370, 81, 17))
        self.lblDescr.setObjectName("lblDescr")
        self.txteditDescr = QtWidgets.QTextEdit(Form)
        self.txteditDescr.setGeometry(QtCore.QRect(10, 390, 383, 31))
        self.txteditDescr.setObjectName("txteditDescr")
        self.lblCrcres = QtWidgets.QLabel(Form)
        self.lblCrcres.setGeometry(QtCore.QRect(10, 430, 81, 17))
        self.lblCrcres.setObjectName("lblCrcres")
        self.txteditCrcRes = QtWidgets.QTextEdit(Form)
        self.txteditCrcRes.setGeometry(QtCore.QRect(10, 450, 383, 31))
        self.txteditCrcRes.setObjectName("txteditCrcRes")
        self.btnGenerate = QtWidgets.QPushButton(Form)
        self.btnGenerate.setGeometry(QtCore.QRect(10, 70, 89, 25))
        self.btnGenerate.setObjectName("btnGenerate")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "All"))
        self.lblMessage.setText(_translate("Form", "Message"))
        self.btnGo.setText(_translate("Form", "Do It"))
        self.lblCrc.setText(_translate("Form", "Crc"))
        self.lblScrambler.setText(_translate("Form", "Scambler"))
        self.lblInter.setText(_translate("Form", "Interliver"))
        self.lblDeint.setText(_translate("Form", "Deinterliver"))
        self.lblDescr.setText(_translate("Form", "Unscramble"))
        self.lblCrcres.setText(_translate("Form", "Crc"))
        self.btnGenerate.setText(_translate("Form", "Generate"))

