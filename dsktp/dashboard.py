from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from PyQt5.QtCore import QUrl

from os import path, getcwd


class Chart(QWebEngineView):
    def __init__(self, parent=None):
        super(Chart, self).__init__(parent)


class Dashboard(QWidget):

    def __init__(self, parent=None):
        super(Dashboard, self).__init__(parent)

        print(path.join(path.abspath(getcwd()), r'test.html'))

        self.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("Submit")

        self.markup = Chart()

        self.markup.load(QUrl().fromLocalFile(
            path.join(path.abspath(getcwd()), r'test.html')
        ))

        self.layout.addWidget(self.markup)
        self.layout.addWidget(self.pushButton1)
        self.setLayout(self.layout)
