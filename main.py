import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from ui import Ui_MainWindow


class JsonV(QtWidgets.QMainWindow):
    def __init__(self):
        super(JsonV, self).__init__()  # Возвращает объект родителя JsonV и возвращает его конструктор
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)             # Вызываем функцию setupUi чтобы отрисовать интерфейс
        self.init_UI()

    def init_UI(self):                      # Функция для работы с графическим интерфейсом
        self.setWindowTitle('JSON visualazion')
        self.setWindowIcon(QIcon('C:\\Users\\1\\Desktop\\hacaton 2021\\1.png'))


app = QtWidgets.QApplication([])
application = JsonV()
application.show()

sys.exit(app.exec())