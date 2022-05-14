import sys

from PySide6 import QtCore
from PySide6.QtCore import QLibraryInfo, QTranslator
from PySide6.QtWidgets import QApplication, QMainWindow

from interfaces.ui_MainWindow import Ui_MainWindow
from tools.default_data_tools import *
from tools.directories_tools import *
from tools.subtasks_tools import *
from tools.buttons_tools import *
from tools.widgets_tools import *
from tools.menu_actions import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ? Datos por defecto de la aplicación *
        # ? ----------------------------------------------------------------- *

        load_default_data_lists(self)
        load_default_variables(self)
        load_default_tape_conditions(self)
        load_default_machining_data(self)

        # ? Folders de almacenamiento *
        # ? ----------------------------------------------------------------- *

        create_machine_folders()

        # ? Botones de la pantalla principal *
        # ? ----------------------------------------------------------------- *

        load_main_buttons(self)
        load_default_buttons_status(self)
        load_main_buttons_connections(self)
        load_menu_actions(self)

        # ? Widgets de la pantalla principal *
        # ? ----------------------------------------------------------------- *

        load_default_window_components(self)
        load_main_widgets_connections(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    translator = QTranslator(app)
    translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    translator.load("qt_es", translations)
    app.installTranslator(translator)

    window = MainWindow()
    window.show()
    window.setWindowState(window.windowState() or QtCore.Qt.WindowMaximized)

    sys.exit(app.exec())
