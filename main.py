import sys

from PySide6 import QtCore
from PySide6.QtCore import QLibraryInfo, QTranslator
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QMainWindow,
    QTableWidgetItem,
)

from interfaces.ui_MainWindow import Ui_MainWindow
from tools.data_tools import *
from tools.directories_tools import *
from tools.subtasks_list import *


class MainWindow(QMainWindow, Ui_MainWindow):

    # ?
    # ?
    # ? Inicialización de la clase principal *
    # ? --------------------------------------------------------------------- *
    # ?
    # ?

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.folders = Config_folders()
        self.folders.create_machine_folders()

        self.load_default_data_lists()
        self.load_default_variables()
        self.load_main_buttons()
        self.load_main_buttons_connections()
        self.load_main_widgets_connections()

    # ?
    # ?
    # ? Datos por defecto de la aplicación *
    # ? --------------------------------------------------------------------- *
    # ?
    # ?

    def load_default_data_lists(self):
        """Carga los valores por defecto de las listas"""

        self.config_list = []
        self.tape1_list = []
        self.tape2_list = []
        self.current_selection = []

    def load_default_variables(self):
        """Carga los valores por defecto de las variables principales"""

        self.subtask1 = None
        self.current_widget = None

    # ?
    # ?
    # ? Botones de la pantalla principal *
    # ? --------------------------------------------------------------------- *
    # ?
    # ?

    def load_main_buttons(self):
        """Carga la lista de botones de la pantalla principal"""

        self.main_buttons_list = (
            self.btn_header,
            self.btn_free,
            self.btn_comment,
            self.btn_subrutine,
            self.btn_collect,
            self.btn_end,
        )

    def load_main_buttons_connections(self):
        """Carga las conexiones de los botones de la pantalla principal"""

        self.btn_header.clicked.connect(lambda: self.collect_data("Header"))
        self.btn_free.clicked.connect(lambda: self.collect_data("Free"))
        self.btn_comment.clicked.connect(lambda: self.collect_data("Comment"))
        self.btn_subrutine.clicked.connect(lambda: self.collect_data("Subrut"))
        self.btn_collect.clicked.connect(lambda: self.collect_data("Collect"))
        self.btn_end.clicked.connect(lambda: self.collect_data("End"))

    # ?
    # ?
    # ? Configuración del tape *
    # ? --------------------------------------------------------------------- *
    # ?
    # ?

    def collect_data(self, data_class: str):
        """Crea una subtarea para recolectar datos

        Args:
            data_class (str): Clase de la subtarea
        """

        subtask_class = tasks_list[data_class]["Name"]
        self.subtask1 = subtask_class()
        self.subtask1.show()
        self.subtask1.collected_data_signal.connect(
            lambda: self.store_data(
                self.subtask1.data_pack,
                self.subtask1.modified_data,
            )
        )

    def store_data(self, data_pack: list, modified_data: bool):
        """Almacena los datos recolectados en la lista de configuración

        Args:
            data_pack (list): Lista de datos recolectados
            modified_data (bool): Indicador de datos modificados
        """

        if modified_data:
            self.update_modified_data(data_pack)
        elif not self.current_selection:
            self.append_new_data(data_pack)
        else:
            self.insert_new_data(data_pack)

        self.update_config_widget()

    def update_modified_data(self, data_pack: list):
        """Actualiza los datos modificados en la lista de configuración

        Args:
            data_pack (list): Paquete de datos modificados
        """

        task = data_pack[0][0]
        data = data_pack[0][1]
        index = self.current_selection[0]
        self.config_list[index] = [task, data]

    def append_new_data(self, data_pack: list):
        """Agrega los datos recolectados al final de la lista

        Args:
            data_pack (list): Paquete de datos recolectados
        """

        for pack in data_pack:
            task = pack[0]
            data = pack[1]
            self.config_list.append([task, data])

            length = len(self.config_list) - 1
            self.current_selection = [length]

    def insert_new_data(self, data_pack: list):
        """Inserta los datos recolectados en una posición de la lista

        Args:
            data_pack (list): Paquete de datos recolectados
        """

        for pack in data_pack:
            task = pack[0]
            data = pack[1]
            index = self.current_selection[0] + 1
            self.config_list.insert(index, [task, data])
            self.current_selection = [index]

    # ?
    # ?
    # ? Líneas de tape *
    # ? --------------------------------------------------------------------- *
    # ?
    # ?

    def generate_tape_lines(self, data):
        pass

    # ?
    # ?
    # ? Widgets *
    # ? --------------------------------------------------------------------- *
    # ?
    # ?

    def load_main_widgets_connections(self):
        """Carga las conexiones de los widgets de la pantalla principal"""

        self.config_widget.clicked.connect(lambda: self.widget_clicked("conf"))
        self.tape1_widget.clicked.connect(lambda: self.widget_clicked("tape1"))
        self.tape2_widget.clicked.connect(lambda: self.widget_clicked("tape2"))

        self.config_widget.itemSelectionChanged.connect(self.config_selected)
        self.tape1_widget.itemSelectionChanged.connect(self.tape1_selected)
        self.tape2_widget.itemSelectionChanged.connect(self.tape2_selected)

    def update_config_widget(self) -> None:
        """Actualiza los datos en el widget de configuración"""

        config = self.config_list
        self.config_widget.setRowCount(len(config))
        for num, line in enumerate(config):
            task_name = line[0]
            self.config_widget.setItem(num, 0, QTableWidgetItem(task_name))

    def widget_clicked(self, widget: str):
        """Recibe la señal de item seleccionado en los widgets

        Args:
            widget (str): Widget del item seleccionado
        """

        self.current_widget = widget

        if widget == "conf":
            self.config_selected()
        elif widget == "tape1":
            self.tape1_selected()
        elif widget == "tape2":
            self.tape2_selected()

    def config_selected(self):
        """Actualiza la lista de índices seleccionados en la configuración"""

        if self.current_widget == "conf":
            if selected_items := self.config_widget.selectedItems():
                config_lines = []
                config_lines.extend(
                    item.row() for item in selected_items if item.column() == 0
                )
                self.current_selection = sorted(list(set(config_lines)))

    def tape1_selected(self):
        """Actualiza la lista de índices seleccionados en el tape1"""

        if self.current_widget == "tape1":
            if selected_items := self.tape1_widget.selectedItems():
                self.items_selection(selected_items)

    def tape2_selected(self):
        """Actualiza la lista de índices seleccionados en el tape2"""

        if self.current_widget == "tape2":
            if selected_items := self.tape2_widget.selectedItems():
                self.items_selection(selected_items)

    def items_selection(self, selected_items):
        """Actualiza la lista de índices seleccionados"""

        selected_list = []
        selected_list.extend(
            item.row() for item in selected_items if item.column() == 0
        )

        config_lines = [self.tape1_list[line][0] for line in selected_list]
        self.current_selection = sorted(list(set(config_lines)))

        if self.current_widget == "tape1":
            self.update_config_widget_selection()
            self.update_tape2_widget_selection()
        elif self.current_widget == "tape2":
            self.update_config_widget_selection()
            self.update_tape1_widget_selection()

    def update_config_widget_selection(self):
        """Actualiza la selección de items en el widget de configuración"""

        all_items = [
            self.config_widget.item(index_number, 0)
            for index_number in range(len(self.config_list))
        ]

        indexes = self.current_selection
        items = [self.config_widget.item(index, 0) for index in indexes]

        self.items_selector(all_items, items, self.config_widget)

    def update_tape1_widget_selection(self):
        """Actualiza la seleccion de items en el widget de tape1"""

        all_items = [
            self.tape1_widget.item(index_number, 0)
            for index_number in range(len(self.tape1_list))
        ]

        config_indexes = self.current_selection
        indexes = [
            num
            for num, index in enumerate(self.tape1_list)
            if index[0] in config_indexes
        ]
        items = [self.tape1_widget.item(index, 0) for index in indexes]

        self.items_selector(all_items, items, self.tape1_widget)

    def update_tape2_widget_selection(self):
        """Actualiza la seleccion de items en el widget de tape2"""

        all_items = [
            self.tape2_widget.item(index_number, 0)
            for index_number in range(len(self.tape2_list))
        ]

        config_indexes = self.current_selection
        indexes = [
            num
            for num, index in enumerate(self.tape2_list)
            if index[0] in config_indexes
        ]
        items = [self.tape2_widget.item(index, 0) for index in indexes]

        self.items_selector(all_items, items, self.tape2_widget)

    def items_selector(self, all_items: list, items: list, widget: object):
        """Selector de items en los widgets

        Args:
            all_items (list): Lista total de items en el widget
            items (list): Lista de items a seleccionar
            widget (QWidget): Widget a seleccionar
        """

        with contextlib.suppress(AttributeError, IndexError):
            for item in all_items:
                item.setSelected(False)
            for item in items:
                item.setSelected(True)
            view = QAbstractItemView
            widget.scrollToItem(items[-1], view.PositionAtCenter)

    # ?
    # ?
    # ? Ventana principal *
    # ? --------------------------------------------------------------------- *
    # ?
    # ?


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
