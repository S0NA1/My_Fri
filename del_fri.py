from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DelFri(object):
    def setupUi(self, DelFri):
        DelFri.setObjectName("DelFri")
        DelFri.resize(672, 541)
        self.pushButton_del = QtWidgets.QPushButton(DelFri)
        self.pushButton_del.setGeometry(QtCore.QRect(270, 450, 371, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_del.sizePolicy().hasHeightForWidth())
        self.pushButton_del.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(32)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setObjectName("pushButton_del")
        self.label_del = QtWidgets.QLabel(DelFri)
        self.label_del.setGeometry(QtCore.QRect(20, 340, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(26)
        self.label_del.setFont(font)
        self.label_del.setObjectName("label_del")
        self.lineEdit_del = QtWidgets.QLineEdit(DelFri)
        self.lineEdit_del.setGeometry(QtCore.QRect(340, 320, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(26)
        self.lineEdit_del.setFont(font)
        self.lineEdit_del.setObjectName("lineEdit_del")
        self.tableWidget_del = QtWidgets.QTableWidget(DelFri)
        self.tableWidget_del.setGeometry(QtCore.QRect(20, 20, 631, 291))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(15)
        self.tableWidget_del.setFont(font)
        self.tableWidget_del.setObjectName("tableWidget_del")
        self.tableWidget_del.setColumnCount(0)
        self.tableWidget_del.setRowCount(0)

        self.retranslateUi(DelFri)
        QtCore.QMetaObject.connectSlotsByName(DelFri)

    def retranslateUi(self, DelFri):
        _translate = QtCore.QCoreApplication.translate
        DelFri.setWindowTitle(_translate("DelFri", "Мой холодильник"))
        self.pushButton_del.setText(_translate("DelFri", "Удалить"))
        self.label_del.setText(_translate("DelFri", "Введите id:"))
