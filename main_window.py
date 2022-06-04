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
        row_count = len(self.auto.vertex)
        column_count = self.auto.count_letters() + 1
        self.tableWidget = QTableWidget(self)
        x = len(self.auto.vertex)
        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(column_count)

        headers = ['v/Σ'] + self.auto.alphabet
        self.tableWidget.setHorizontalHeaderLabels(headers)

        table = self.auto.get_table()
        for i in range(row_count):
            for j in range(column_count):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(table[i][j])))
        self.tableWidget.resize(1000, 1000)
        self.tableWidget.move(0, 30)

        link_table = self.auto.get_link_table()
        link_table_widget = QTableWidget(self)
        link_table_widget.setRowCount(len(link_table))
        link_table_widget.setColumnCount(4)
        link_table_widget.setHorizontalHeaderLabels(['вершина', 'вершина', 'суф. ссылка', 'суф.ссылка'])
        for i in range(len(link_table)):
            link_table_widget.setItem(i, 0, QTableWidgetItem(str(i)))
            text = self.auto.vertex[i].text
            if text == '':
                text = 'λ'
            link_table_widget.setItem(i, 1, QTableWidgetItem(text))
            link_table_widget.setItem(i, 2, QTableWidgetItem(str(link_table[i][1])))
            text = self.auto.vertex[link_table[i][1]].text
            if text == '':
                text = 'λ'
            link_table_widget.setItem(i, 3, QTableWidgetItem(text))
        link_table_widget.resize(640, 1000)
        link_table_widget.move(1010, 30)

        text = 'Конечные состояния:'
        for i in self.auto.final_v:
            text += ' ' + str(i)
        label_final = QLabel(text, self)
        label_final.setFont(QFont('Arial', 10))
        label_final.move(0, 0)

        label_start = QLabel('Начальное состояние: 0', self)
        label_start.setFont(QFont('Arial', 10))
        label_start.move(500, 0)

        self.resize(1200, 1050)
        self.center()
        self.setWindowTitle('Таблица переходов')
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))
