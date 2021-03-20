import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QDir
from ui import Ui_MainWindow


class JsonV(QtWidgets.QMainWindow):
    def __init__(self):
        super(JsonV, self).__init__()  # Возвращает объект родителя JsonV и возвращает его конструктор
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)             # Вызываем функцию setupUi чтобы отрисовать интерфейс
        self.init_UI()

    def init_UI(self):                      # Функция для работы с графическим интерфейсом
        self.setWindowTitle('JSON visualazion')
        self.setWindowIcon(QIcon('C:\\Users\\1\\PycharmProjects\\pythonProject\\1.png'))
        self.ui.openFile.clicked.connect(self.open_json)
        self.ui.openDiagram.clicked.connect(self.open_diagram)
        self.ui.viewFile.clicked.connect(self.view_json)

    def open_json(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open JSON file', filter="JSON files (*.json)")

    def open_diagram(self):
        pass

    def view_json(self):
        pass


app = QtWidgets.QApplication([])
application = JsonV()
application.show()

sys.exit(app.exec())