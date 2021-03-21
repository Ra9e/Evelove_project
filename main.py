import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog      # Для работы с загрузкой фалов
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QDir
from ui import Ui_MainWindow                 # Импорт основного UI
from json_visual import prt_data

from pyvis.network import Network
import json

from wordcloud import WordCloud
import matplotlib.pyplot as plt


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
        global file_name
        file_name = QFileDialog.getOpenFileName(self, 'Open JSON file', filter="JSON files (*.json)")

    def open_diagram(self):                  # Функция для загрузки json файла, обработка 2 кнопки
        #file_pic = QFileDialog.getOpenFileName(self, 'Open JSON file', filter="JSON files (*.jpeg, *.jpg)")
        #text = (prt_data())
        text = "1 H 2 H 3 A1 A1 H"

        wordCLD = WordCloud(width=900, height=750, margin=0).generate(text)
        plt.imshow(wordCLD, interpolation='bilinear')
        plt.axis("off")
        plt.margins(x=0, y=0)
        plt.savefig('saved_figure.png')
        self.ui.diagram_.setPixmap(QPixmap("C:\\Users\\1\\PycharmProjects\\pythonProject\\saved_figure.png"))

    def view_json(self):
        try:
            def get_data():
                with open(file_name[0], "r") as json_file:
                    data = json.load(json_file)
                    return (data)               # data["alcuin_letters"]

            def map_algs(graph, alg="barnes"):  # Алгоритмы графиков
                if alg == "barnes":
                    graph.barnes_hut()  # Для работы с большими данными
                if alg == "forced":
                    graph.force_atlas_2based()
                if alg == "hr":
                    graph.hrepulsion()

            def map_data(letter_data, ep_color="#03DAC6", ms_color="#da03b3", edge_color="#018786",
                         ep_shape="triangle", ms_shape="box", alg="barnes", buttons=False,
                         recipient_color="#FFA300", recipient_shape="ellipse",
                         cited_color="#DFEE9A", cited_shape="square"):
                graph = Network(height="1000px", width="100%", bgcolor="#222222", font_color="white", directed=True)
                graph.add_node("Alcuin 1", color="#EB9090")

                if buttons == True:
                    graph.width = "62%"
                    graph.show_buttons(filter_=["edges"])  # Кнопки для работы с графиков в реальном времени

                for letter in letter_data[0:10]:

                    ep = (letter["ep_num"])[0]
                    graph.add_node(ep, color=ep_color, shape=ep_shape)  # Добавляем узел и наносим его на график
                    graph.add_edge("Alcuin 1", ep, color=edge_color)

                    mss = (letter["mss"])
                    for ms in mss:
                        graph.add_node(ms, color=ms_color, shape=ms_shape)  # Добавляем узел и наносим его на график
                        graph.add_edge(ep, ms, color=edge_color)

                    recipients = (letter["recipients"])
                    for recipient in recipients:
                        graph.add_node(recipient, color=recipient_color, shape=recipient_shape)
                        graph.add_edge(ep, recipient, color=recipient_color)
                        graph.add_edge("Alcuin 1", recipient, color="#EB9090")

                    people_cited = (letter["people_cited"])
                    for cited in people_cited:
                        if "Alcuin 1" not in cited:
                            graph.add_node(cited, color=cited_color, shape=cited_shape)
                            graph.add_edge(ep, cited, color=cited_color)

                map_algs(graph, alg=alg)
                graph.show("letters.html")

            epp_data = get_data()
            map_data(letter_data=epp_data, alg="force", buttons=True)
        except:
            pass


app = QtWidgets.QApplication([])
application = JsonV()
application.show()

sys.exit(app.exec())
