from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    FIT_WINDOW, FIT_WIDTH, MANUAL_ZOOM = list(range(3))

    def __init__(self) -> None:
        super(MainWindow, self).__init__()

def get_main_app(argv=[]):

    app = QApplication(argv)
    win = MainWindow()
    win.show()
    return app, win


def main():
    app, _win = get_main_app(sys.argv)
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())