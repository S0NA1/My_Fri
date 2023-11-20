import sys
import sqlite3
import typing
import datetime

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget
from PyQt5 import QtGui, QtWidgets

from mainwin import Ui_MainWindow
from add_prod import Ui_add_fri
from del_fri import Ui_DelFri
from last_fri import Ui_PastOfFri

con = sqlite3.connect("my_db.db")
cur = con.cursor()
query = """CREATE TABLE IF NOT EXISTS
                al_base(id INTEGER PRIMARY KEY, 
                subject TEXT, 
                date INTEGER, 
                alive BOOL)"""
cur.execute(query)
con.commit()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size().width(), self.size().height())

        self.pushButton_addfri.clicked.connect(self.ad_cons)
        self.pushButton_myfri.clicked.connect(self.my_del_fri)
        self.pushButton_pastfri.clicked.connect(self.dob_last)

    def ad_cons(self):
        self.second_form = MyAdd(self)
        self.second_form.show()
        self.hide()

    def my_del_fri(self):
        self.second_form = DelFri(self)
        self.second_form.show()
        self.hide()

    def dob_last(self):
        self.second_form = PastOfFri(self)
        self.second_form.show()
        self.hide()


class MyAdd(QWidget, Ui_add_fri):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parentWindow = parent
        self.setupUi(self)
        self.setFixedSize(self.size().width(), self.size().height())

        self.pushButton__add.clicked.connect(self.add_subject)

    def closeEvent(self, a0: typing.Optional[QtGui.QCloseEvent]) -> None:
        self.parentWindow.show()
        a0.accept()

    def add_subject(self):
        obj = self.lineEdit_add.text()
        dat = self.dateEdit__add.text()
        self.listWidget_add.addItem(obj)

        connection = sqlite3.connect('my_db.db')
        cursor = connection.cursor()
        query = f"""INSERT INTO al_base(subject, date, alive) 
        VALUES("{obj}", "{dat}", 1)"""
        cursor.execute(query)
        connection.commit()
        connection.close()

        self.lineEdit_add.clear()


class DelFri(QWidget, Ui_DelFri):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parentWindow = parent
        self.setupUi(self)
        self.setFixedSize(self.size().width(), self.size().height())

        con = sqlite3.connect("my_db.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM al_base
                                            WHERE alive = 1""").fetchall()
        result = list(map(lambda x: list(map(lambda y: str(y), x)), result))
        self.tableWidget_del = QTableWidget(len(result), 3, self)
        self.tableWidget_del.setHorizontalHeaderLabels(['id', 'object', 'date'])
        self.tableWidget_del.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget_del.setGeometry(20, 20, 631, 291)
        for i, row_data in enumerate(result):
            for j, cell_data in enumerate(row_data[:-1]):
                item = QtWidgets.QTableWidgetItem(cell_data)
                self.tableWidget_del.setItem(i, j, item)
        self.pushButton_del.clicked.connect(self.del_id)

        def color_table(days):
            k = 0
            for r in days:
                if r < 0:
                    self.tableWidget_del.item(k, 0).setBackground(QtGui.QColor(255, 0, 0))
                    self.tableWidget_del.item(k, 1).setBackground(QtGui.QColor(255, 0, 0))
                    self.tableWidget_del.item(k, 2).setBackground(QtGui.QColor(255, 0, 0))
                    k += 1
                elif 1 <= r <= 4:
                    self.tableWidget_del.item(k, 0).setBackground(QtGui.QColor(255, 255, 0))
                    self.tableWidget_del.item(k, 1).setBackground(QtGui.QColor(255, 255, 0))
                    self.tableWidget_del.item(k, 2).setBackground(QtGui.QColor(255, 255, 0))
                    k += 1
                else:
                    self.tableWidget_del.item(k, 0).setBackground(QtGui.QColor(0, 255, 0))
                    self.tableWidget_del.item(k, 1).setBackground(QtGui.QColor(0, 255, 0))
                    self.tableWidget_del.item(k, 2).setBackground(QtGui.QColor(0, 255, 0))
                    k += 1

        date_list = list(map(lambda x: x[2], result))
        dt_now = datetime.datetime.now().date()
        day_list = []
        for i in date_list:
            d_n = str(i).split(".")
            now = datetime.datetime(int(d_n[2]), int(d_n[1]), int(d_n[0])).date()
            days = str(now - dt_now).split(", ")
            days = days[0].split()
            days = days[0]
            day_list.append(int(days))
        color_table(day_list)

    def closeEvent(self, a0: typing.Optional[QtGui.QCloseEvent]) -> None:
        self.parentWindow.show()
        a0.accept()

    def del_id(self):
        id_now = int(self.lineEdit_del.text())
        con = sqlite3.connect("my_db.db")
        cur = con.cursor()
        dop = f"""UPDATE al_base SET alive = 0 
              WHERE id = {id_now}"""
        cur.execute(dop)
        con.commit()
        con.close()
        self.lineEdit_del.clear()


class PastOfFri(QWidget, Ui_PastOfFri):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parentWindow = parent
        self.setupUi(self)
        self.now_set = set()
        self.setFixedSize(self.size().width(), self.size().height())
        self.pushButton_last.clicked.connect(self.last_add)
        con = sqlite3.connect("my_db.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM al_base
                                                    WHERE alive = 0""").fetchall()
        self.listWidget.addItem("\t".join(["id", "object"]))
        self.listWidget.addItem("___________________________________________________________________")
        for elem in result:
            elem = list(map(lambda x: str(x), elem))
            elem = elem[:-2]
            if elem[1] in self.now_set:
                continue
            else:
                self.now_set.add(elem[1])
                self.listWidget.addItem("\t".join(elem))

    def closeEvent(self, a0: typing.Optional[QtGui.QCloseEvent]) -> None:
        self.parentWindow.show()
        a0.accept()

    def last_add(self):
        con = sqlite3.connect('my_db.db')
        id_now = int(self.lineEdit_last.text())
        dat = self.dateEdit_last.text()
        cur = con.cursor()
        now = cur.execute(f"SELECT subject FROM al_base WHERE id = {id_now}").fetchall()
        cur.execute(f"""INSERT INTO al_base(subject, date, alive) 
        VALUES("{now[0][0]}", "{dat}", 1)""")
        con.commit()
        con.close()
        self.lineEdit_last.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    app.exec_()
