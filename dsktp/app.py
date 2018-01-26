#!/usr/bin/python3.6

import sys
import argparse

from subprocess import call
from PyQt5.QtWidgets import (QApplication, QMenu, QPushButton, QLineEdit, QWidget, QMessageBox, QDesktopWidget, QMainWindow, QAction, QLabel, QGridLayout, qApp) 
from PyQt5.QtCore import Qt, pyqtSignal, QRegExp
from PyQt5.QtGui import QIcon, QFont, QValidator, QRegExpValidator

class App(QWidget):

    def __init__(self, args=None):
        super().__init__()
        
        self.cmd_call = "${{SPARK_HOME}}/bin/spark-submit \
            --master ${{MASTER}} \
            --py-files ${{TFoS_HOME}}/examples/mnist/spark/mnist_dist.py \
            --conf spark.cores.max=${TOTAL_CORES} \
            --conf spark.task.cpus=${CORES_PER_WORKER} \
            --conf spark.executorEnv.JAVA_HOME=\"$JAVA_HOME\" \
            ${{TFoS_HOME}}/examples/mnist/spark/mnist_spark.py \
            --cluster_size ${SPARK_WORKER_INSTANCES} \
            --images examples/mnist/csv/train/images \
            --labels examples/mnist/csv/train/labels \
            --format csv \
            --mode train \
            --model mnist_model"
        self.init_ui()

    def init_ui(self):
        # exitAct = QAction(QIcon('exit.png'), ' Exit', self)
        exitAct = QAction(' Exit', self)
        exitAct.setShortcut('Cmd+Q')
        exitAct.triggered.connect(qApp.quit)

        #self.statusBar()

        #menubar = self.menuBar()
        #filemenu = menubar.addMenu('File')
       
        self.num_workers = QLabel('Workers:')
        self.num_cores = QLabel('Cores:')
        self.mem = QLabel('Memory per worker:')
        self.tf_path = QLabel('Path to TensorFlow:')
        self.data_path = QLabel('Path to data:')

        self.worker_edit = QLineEdit()
        self.worker_edit.setMaximumWidth(30)

        self.core_edit = QLineEdit()
        self.core_edit.setMaximumWidth(30)

        self.mem_edit = QLineEdit()
        self.mem_edit.setMaximumWidth(30)

        self.tf_edit = QLineEdit()
        self.data_edit = QLineEdit()

        # regexp = QRegExp('^(\d\d?)$')
        # validator = QRegExpValidator(regexp)
        # worker_edit.setValidator(validator)

        # self.worker_edit.editingFinished.connect(self.check_state)
        # worker_edit.editingFinished.connect(lambda x: print(x))
        # worker_edit.editingFinished.emit(worker_edit.text())

        grid = QGridLayout()

        grid.addWidget(self.num_workers, 1, 0)
        grid.addWidget(self.worker_edit, 1, 1)

        grid.addWidget(self.num_cores, 2, 0)
        grid.addWidget(self.core_edit, 2, 1)

        grid.addWidget(self.mem, 3, 0)
        grid.addWidget(self.mem_edit, 3, 1)
        
        grid.addWidget(self.tf_path, 4, 0)
        grid.addWidget(self.tf_edit, 4, 1)
        
        grid.addWidget(self.data_path, 5, 0)
        grid.addWidget(self.data_edit, 5, 1)

        submit_btn = QPushButton("Submit", self)
        submit_btn.clicked.connect(self.submit_job)

        grid.addWidget(submit_btn, 6, 0)
        self.setLayout(grid)
               
        self.resize(1000, 700)
        self.center()
        self.setWindowTitle('Test Bed')    
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def keyPressEvent(self, e):
        print(e.key())
        
        if e.key() == Qt.Key_Escape:
            self.close()


    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
                   
        # newAct = cmenu.addAction("New")
        quitAct = cmenu.addAction("Quit")
        cmenu.setFixedWidth(100)
        cmenu.setFixedWidth(200)
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
           
        if action == quitAct:
            qApp.quit()

    def check_state(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        
        if state is not QValidator.Acceptable:  # and state is not QValidator.Intermediate:
            color = '#f6989d' # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def submit_job(self, *args, **kwargs):
        print("Check1: ", *args, **kwargs)
        # args = [self.worker_edit.text(), self.core_edit.text(), self.tf_edit.text(), self.data_edit.text()]
        self.cmd_call.format(SPARK_WORKER_INSTANCES=self.worker_edit.text(), TOTAL_CORES=self.mem_edit.text(), CORES_PER_WORKER=self.core_edit.text())
        print(self.cmd_call)
        if "rm" not in self.cmd_call:
            print(self.cmd_call)
            # call(self.cmd_call)
        else:
            print("Please don't remove anything")
        
        print("Number of Workers: {}\nNumber of CPU's/Worker: {}\nTensorFlow path: {}\nData path: {}"
            .format(self.worker_edit.text(), self.core_edit.text(), self.tf_edit.text(), self.data_edit.text()))


if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    app = App()
    sys.exit(qapp.exec_())
    
