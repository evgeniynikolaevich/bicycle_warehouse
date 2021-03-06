from operations.ui.main_template import Ui_MainWindow
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWidget, QDialog
from widgets.custom_widgets import CustomMainWindow


class Main(Ui_MainWindow):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = CustomMainWindow()
    ui = Main()
    ui.setupUi(MainWindow)
    # screenShape = QtWidgets.QDesktopWidget().screenGeometry()
    # MainWindow.resize(screenShape.width(), screenShape.height())
    MainWindow.show()
    sys.exit(app.exec_())
