import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog      # Для работы с загрузкой фалов
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QDir
from ui import Ui_MainWindow                 # Импорт основного UI

from pyvis.network import Network
import networkx as nx

"""from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow"""

class JsonV(QtWidgets.QMainWindow):
    def __init__(self):
        super(JsonV, self).__init__()        # Возвращает объект родителя JsonV и возвращает его конструктор
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)                # Вызываем функцию setupUi чтобы отрисовать интерфейс
        self.init_UI()

    def init_UI(self):                       # Функция для доработки графического интерфейса
        self.setWindowTitle('JSON visualization')
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
        """web = QWebEngineView()
        html_name = 'nx.html'

        nx_graph = nx.cycle_graph(10)
        nx_graph.nodes[1]['title'] = 'Number 1'
        nx_graph.nodes[1]['group'] = 1
        nx_graph.nodes[3]['title'] = 'I belong to a different group!'
        nx_graph.nodes[3]['group'] = 10
        nx_graph.add_node(20, size=20, title='couple', group=2)
        nx_graph.add_node(21, size=15, title='couple', group=2)
        nx_graph.add_edge(20, 21, weight=5)
        nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)
        nt = Network('500px', '500px')

        # populates the nodes and edges data structures
        nt.from_nx(nx_graph)
        nt.show(html_name)
        nt.save_graph(html_name)

        web.load(QUrl("https://pythonspot.com"))
        web.show()"""


app = QtWidgets.QApplication([])
application = JsonV()
application.show()

sys.exit(app.exec())
