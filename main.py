import sys

from PySide6 import QtCore
from PySide6.QtCore import QTranslator, QLibraryInfo
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from tools.data_tools import *
from tools.subtasks_list import *
from tools.directories_tools import *

from interfaces.ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.subtask1 = None
        self.setupUi(self)
        self.data = Data_lists()
        self.folders = Config_folders()
        self.folders.create_machine_folders()

        self.btn_header.clicked.connect(lambda: self.collect_data("Header"))

    # * Funciones de recolección y procesamiento de datos capturados
    # * --------------------------------------------------------------------- *

    def collect_data(self, data_class):
        subtask_class = tasks_list[data_class]["Name"]
        self.subtask1 = subtask_class()
        self.subtask1.show()
        self.subtask1.collected_data_signal.connect(
            lambda: self.process_data(self.subtask1.data_pack)
        )

    def process_data(self, data):
        if data:
            self.data.config_list.append(data[1])
            self.update_config_widget()

    # * Funciones de actualización de widgets
    # * --------------------------------------------------------------------- *

    def update_config_widget(self) -> None:
        config = self.data.config_list
        self.config_widget.setRowCount(len(config))
        for num, line in enumerate(config):
            task_name = line[0]
            self.config_widget.setItem(num, 0, QTableWidgetItem(task_name))


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
