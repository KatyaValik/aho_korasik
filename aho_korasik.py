import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QFont
from main_window import MainWindow


class StartWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.words_box = None
        self.words = None
        self.main_window = None

        self.initUI()

    def initUI(self):
        label = QLabel('Введите слова через пробел:', self)
        label.move(50, 100)
        label.resize(900, 50)
        label.setFont(QFont('Arial', 15))

        self.words_box = QLineEdit(self)
        self.words_box.move(50, 200)
        self.words_box.resize(900, 50)
        self.words_box.setFont(QFont('Arial', 15))

        button = QPushButton('построить автомат', self)
        button.move(300, 500)
        button.resize(400, 50)
        button.setFont(QFont('Arial', 15))
        button.clicked.connect(self.on_click_button)

        self.resize(1000, 1000)
        self.center()
        self.setWindowTitle('Ахо-Корасик')
        self.show()

    def on_click_button(self):
        self.words = self.words_box.text().split()
        self.main_window = MainWindow(self.words)
        self.main_window.show()
        self.hide()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    sys.exit(app.exec_())

