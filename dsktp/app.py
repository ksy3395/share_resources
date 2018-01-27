#!/usr/bin/python3.6

import sys
import shlex
import os

from subprocess import call, Popen
from PyQt5.QtWidgets import (QApplication, QMenu, QPushButton, QCheckBox, QLineEdit, QWidget, QMessageBox, QDesktopWidget, QMainWindow, QAction, QLabel, QGridLayout, qApp) 
from PyQt5.QtCore import Qt, pyqtSignal, QRegExp
from PyQt5.QtGui import QIcon, QFont, QValidator, QRegExpValidator

class App(QWidget):

    def __init__(self, args=None):
        super().__init__()
        self.title = "Test Bed"
        self.cmd_call_train = r"$SPARK_HOME/bin/spark-submit \
            --master $MASTER \
            --py-files $TFoS_HOME{SOURCE_FILES} \
            --conf spark.cores.max={TOTAL_CORES} \
            --conf spark.task.cpus={CORES_PER_WORKER} \
            --conf spark.executor.memory={MEMORY} \
            --conf spark.executorEnv.JAVA_HOME=\"$JAVA_HOME\" \
            $TFoS_HOME/examples/mnist/spark/mnist_spark.py \
            --cluster_size={SPARK_WORKER_INSTANCES} \
            --images {IMAGES}  \
            --labels {LABELS} \
            --format csv \
            --mode train \
            --model mnist_model"

        self.cmd_call_inference = r"$SPARK_HOME/bin/spark-submit \
            --master $MASTER \
            --py-files $TFoS_HOME{SOURCE_FILES} \
            --conf spark.cores.max={TOTAL_CORES} \
            --conf spark.task.cpus={CORES_PER_WORKER} \
            --conf spark.executor.memory={MEMORY} \
            --conf spark.executorEnv.JAVA_HOME=\"$JAVA_HOME\" \
            $TFoS_HOME/examples/mnist/spark/mnist_spark.py \
            --cluster_size={SPARK_WORKER_INSTANCES} \
            --images {IMAGES}  \
            --labels {LABELS} \
            --format csv \
            --mode inference \
            --model mnist_model \
            --output predictions"

        self.init_ui()

    def init_ui(self):
        exitAct = QAction(' Exit', self)
        exitAct.setShortcut('Cmd+Q')
        exitAct.triggered.connect(qApp.quit)

        #self.statusBar()

        self.title_bar = QLabel(self.title)
        self.title_bar.setFont(QFont("Times", weight=QFont.Bold))

        self.num_workers = QLabel('Workers:')
        self.num_cores = QLabel('Cores:')
        self.mem = QLabel('Memory per worker:')
        self.tf_path = QLabel('Path to source files:')
        self.data_path = QLabel('Path to data:')

        self.worker_edit = QLineEdit()
        self.worker_edit.setMaximumWidth(40)

        self.core_edit = QLineEdit()
        self.core_edit.setMaximumWidth(40)

        self.mem_edit = QLineEdit()
        self.mem_edit.setMaximumWidth(40)

        self.tf_edit = QLineEdit()
        self.data_edit = QLineEdit()

        layout = QGridLayout()
        grid_top = QGridLayout()
        
        layout.addWidget(self.title_bar, 1, 0, Qt.AlignLeft)

        grid_top.addWidget(self.num_workers, 1, 0, Qt.AlignRight)
        grid_top.addWidget(self.worker_edit, 1, 1, Qt.AlignLeft)

        grid_top.addWidget(self.num_cores, 1, 2, Qt.AlignRight)
        grid_top.addWidget(self.core_edit, 1, 3, Qt.AlignLeft)

        grid_top.addWidget(self.mem, 1, 4, Qt.AlignRight)
        grid_top.addWidget(self.mem_edit, 1, 5, Qt.AlignLeft)
        
        layout.addWidget(self.tf_path, 3, 0)
        layout.addWidget(self.tf_edit, 3, 1)
        
        layout.addWidget(self.data_path, 4, 0)
        layout.addWidget(self.data_edit, 4, 1)

        submit_btn = QPushButton("Submit", self)
        submit_btn.clicked.connect(self.submit_job)

        self.inference_btn = QCheckBox("Inference Mode", self)

        layout.addWidget(submit_btn, 5, 0, Qt.AlignHCenter)
        layout.addWidget(self.inference_btn, 5, 1, Qt.AlignHCenter)

        layout.addLayout(grid_top, 2, 1, 1, 2, Qt.AlignHCenter)
        self.setLayout(layout)
               
        self.resize(200, 100)
        self.center()
        self.setWindowTitle(self.title)
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

    def submit_job(self, *args, **kwargs):
        images = self.data_edit.text() + "images"
        labels = self.data_edit.text() + "labels"
        memory = self.mem_edit.text()

        if self.inference_btn.isChecked():
            cmd_call = self.cmd_call_inference
        else:
            cmd_call = self.cmd_call_train 

        cmd_call = cmd_call.format(
                    SOURCE_FILES=self.tf_edit.text(),
                    TOTAL_CORES=int(self.core_edit.text()) * int(self.worker_edit.text()),
                    SPARK_WORKER_INSTANCES=self.worker_edit.text(), 
                    MEMORY=memory,
                    CORES_PER_WORKER=self.core_edit.text(),
                    IMAGES=images,
                    LABELS=labels
                    )
        args = shlex.split(cmd_call)
        print(args)
        os.system(cmd_call)
        
        print("Number of Workers: {}\nNumber of CPU's/Worker: {}\nTensorFlow path: {}\nData path: {}"
            .format(self.worker_edit.text(), self.core_edit.text(), self.tf_edit.text(), self.data_edit.text()))


if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    app = App()
    sys.exit(qapp.exec_())
    
