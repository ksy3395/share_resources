
from PyQt5.QtWidgets \
    import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from dsktp.dashboard import Dashboard
from dsktp.resources import Resources
from dsktp.jobs import Jobs


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Share Resources"
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 480
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()

        self.table_widget = MainWindow(self)
        self.setCentralWidget(self.table_widget)

        self.show()

    def center(self):
        rect = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        rect.moveCenter(center)
        self.move(rect.topLeft())


class MainWindow(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = Dashboard()  # Dashboard tab; contained in dashboard.py
        self.tab2 = Resources()  # Resource tab; contained in resources.py
        self.tab3 = Jobs()  # Jobs tab; contained in jobs.py
        self.tabs.resize(640, 480)

        # Add tabs
        self.tabs.addTab(self.tab1, "Dashboard")
        self.tabs.addTab(self.tab2, "Resources")
        self.tabs.addTab(self.tab3, "Jobs")

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
