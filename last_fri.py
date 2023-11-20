from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PastOfFri(object):
    def setupUi(self, PastOfFri):
        PastOfFri.setObjectName("PastOfFri")
        PastOfFri.resize(586, 535)
        self.pushButton_last = QtWidgets.QPushButton(PastOfFri)
        self.pushButton_last.setGeometry(QtCore.QRect(210, 470, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.pushButton_last.setFont(font)
        self.pushButton_last.setObjectName("pushButton_last")
        self.lineEdit_last = QtWidgets.QLineEdit(PastOfFri)
        self.lineEdit_last.setGeometry(QtCore.QRect(30, 350, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.lineEdit_last.setFont(font)
        self.lineEdit_last.setObjectName("lineEdit_last")
        self.dateEdit_last = QtWidgets.QDateEdit(PastOfFri)
        self.dateEdit_last.setGeometry(QtCore.QRect(360, 350, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.dateEdit_last.setFont(font)
        self.dateEdit_last.setObjectName("dateEdit_last")
        self.label_last = QtWidgets.QLabel(PastOfFri)
        self.label_last.setGeometry(QtCore.QRect(40, 280, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.label_last.setFont(font)
        self.label_last.setObjectName("label_last")
        self.listWidget = QtWidgets.QListWidget(PastOfFri)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 561, 271))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(PastOfFri)
        QtCore.QMetaObject.connectSlotsByName(PastOfFri)

    def retranslateUi(self, PastOfFri):
        _translate = QtCore.QCoreApplication.translate
        PastOfFri.setWindowTitle(_translate("PastOfFri", "Прошлое холодильника"))
        self.pushButton_last.setText(_translate("PastOfFri", "Добавить"))
        self.label_last.setText(_translate("PastOfFri", "Введите id товара:"))
