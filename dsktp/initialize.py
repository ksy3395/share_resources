from dsktp.app import App
from dsktp.login import Login

from PyQt5.QtWidgets import QApplication, QDialog

if __name__ == '__main__':
    from sys import exit, argv

    app = QApplication(argv)  # Instantiates application thread I think?
    # login = Login()  # This guy is inherits from QDialog which run in a different event thread
    #
    # login_success = login.exec_()  # Returns a truthy value (hopefully)
    # if login_success == QDialog.Accepted:
    #     # del login  # Get rid of that so we don't trample the GIL (I think?)

    main_app = App()  # Our application
    exit(app.exec_())  # Return control to the original thread

