import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLineEdit, QLabel, QPushButton, QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QFont
from automat import Automat

class MainWindow(QWidget):
    def __init__(self, words):
        super().__init__()

        self.words = words
        self.auto = Automat(self.words)
        self.auto.create_auto()

        self.initUI()

    def initUI(self):
        row_count = len(self.auto.vertex) + 1
        column_count = self.auto.count_letters() + 1
        self.tableWidget = QTableWidget(self)
        x = len(self.auto.vertex)
        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(column_count)

        headers = ['v/Σ'] + self.auto.alphabet()
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for i in range(row_count):
            for j in range(column_count):
                self.tableWidget.setItem(i, j, QTableWidgetItem('a'))

        self.tableWidget.resize(1000, 1000)
        self.tableWidget.move(0, 0)



        self.resize(1000, 1000)
        self.center()
        self.setWindowTitle('Таблица переходов')
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))