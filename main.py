import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog      # Для работы с загрузкой фалов
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QDir
from ui import Ui_MainWindow                 # Импорт основного UI


class JsonV(QtWidgets.QMainWindow):
    def __init__(self):
        super(JsonV, self).__init__()        # Возвращает объект родителя JsonV и возвращает его конструктор
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)                # Вызываем функцию setupUi чтобы отрисовать интерфейс
        self.init_UI()

    def init_UI(self):                       # Функция для доработки графического интерфейса
        self.setWindowTitle('JSON visualazion')
        self.setWindowIcon(QIcon('C:\\Users\\1\\PycharmProjects\\pythonProject\\1.png'))
        self.ui.openFile.clicked.connect(self.open_json)
        self.ui.openDiagram.clicked.connect(self.open_diagram)
        self.ui.viewFile.clicked.connect(self.view_json)
        self.setFixedSize(471, 431)

    def open_json(self):                     # Функция для загрузки json файла, обработка 1 кнопки
        file_name = QFileDialog.getOpenFileName(self, 'Open JSON file', filter="JSON files (*.json)")

    def open_diagram(self):                  # Функция для загрузки json файла, обработка 2 кнопки
        file_pic = QFileDialog.getOpenFileName(self, 'Open JSON file', filter="JSON files (*.jpeg, *.jpg)")
        self.ui.diagram_.setPixmap(QPixmap(file_pic[0]))

    def view_json(self):
        pass


app = QtWidgets.QApplication([])
application = JsonV()
application.show()

sys.exit(app.exec())