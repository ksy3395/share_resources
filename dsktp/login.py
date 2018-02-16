from PyQt5.QtWidgets \
    import QApplication, QDialog, QLabel, QGroupBox, QFormLayout, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, \
    QMainWindow, QStatusBar


class Login(QDialog):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.username = QLineEdit(self)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)  # Asterisks
        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.handle_login)

        self.login_group_box = None
        self.create_login_form()

        login_layout = QVBoxLayout()
        login_layout.addWidget(self.login_group_box)
        login_layout.addWidget(self.login_button)
        self.setLayout(login_layout)

    def handle_login(self):
        if self.username.text().lower() == "foo" and self.password.text().lower() == "bar":
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "The username or password you have entered is invalid.")

    def create_login_form(self):
        self.login_group_box = QGroupBox("Share Resources")
        layout = QFormLayout()
        layout.addRow(QLabel("Username: "), self.username)
        layout.addRow(QLabel("Password: "), self.password)
        self.login_group_box.setLayout(layout)
