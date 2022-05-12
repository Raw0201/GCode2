import sys

from PySide6 import QtCore
from PySide6.QtCore import QLibraryInfo, QTranslator
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
)

from interfaces.ui_MainWindow import Ui_MainWindow
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
        self.config_file_name = ""
        self.current_machine = ""
        self.current_config_line = 0
        self.current_tool = 0
        self.current_comment = ""

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
    # ? Datos de configuración del tape *
    # ? --------------------------------------------------------------------- *
    # ?
    # ?

    def collect_data(self, data_class: str):
        """Crea una subtarea para recolectar datos de configuración

        Args:
            data_class (str): Clase de la subtarea
        """

        subtask_class = tasks_list[data_class]["Name"]
        self.subtask1 = subtask_class(window)

        if data_class not in {"Free"}:
            self.subtask1.show()
        else:
            self.subtask1.collector()

    def store_config_data(self, data_pack: list, modification: bool):
        """Almacena los datos recolectados en la lista de configuración

        Args:
            data_pack (list): Lista de datos recolectados
            modification (bool): Indicador de datos modificados
        """

        if modification:
            self.update_modified_data(data_pack)
        elif not self.current_selection:
            self.append_new_data(data_pack)
        else:
            self.insert_new_data(data_pack)

        self.load_defaults()
        self.generate_tape_lines(self.config_list)
        self.update_data_widgets()

    def load_defaults(self):
        """Carga los valores por defecto"""

        self.load_default_variables()

    def update_data_widgets(self):
        """Actualiza los datos en los widgets"""

        self.update_config_widget()
        self.update_tape_widget(self.tape1_widget, self.tape1_list)
        self.update_tape_widget(self.tape2_widget, self.tape2_list)

        self.update_config_widget_selection()
        self.update_tape1_widget_selection()
        self.update_tape2_widget_selection()

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

            end_line = len(self.config_list) - 1
            self.current_selection = [end_line]

    def insert_new_data(self, data_pack: list):
        """Inserta los datos recolectados en una posición de la lista

        Args:
            data_pack (list): Paquete de datos recolectados
        """

        for pack in data_pack:
            task = pack[0]
            data = pack[1]
            current_index = self.current_selection[0] + 1
            self.config_list.insert(current_index, [task, data])
            self.current_selection = [current_index]

    # ?
    # ?
    # ? Líneas de tape *
    # ? --------------------------------------------------------------------- *
    # ?
    # ?

    def generate_tape_lines(self, data_list: list):
        """Genera las líneas de tape a partir de la lista de configuración

        Args:
            data_list (list): Lista de configuración
        """

        self.tape1_list = []
        self.tape2_list = []

        for line in data_list:
            task = line[0]
            data = line[1]
            if task != "Inicio de programa":
                self.current_config_line += 1

            task_class = get_task_class(task)
            task_class.processor(self, window, data)
            task_class.switcher(self, window, data)

            parameters = self.get_parameters()
            machine = self.current_machine
            tape_lines = task_class.generator(self, machine, data)

            self.store_tape_data(tape_lines, parameters)

    def store_tape_data(self, tape_lines: list, parameters: dict) -> None:
        """Guarda las líneas de tape en las listas respectivas

        Args:
            tape_lines (list): Líneas generadas de tape
            parameters (dict): Diccionario de parámetros actuales
        """

        config_line = parameters["Config_line"]
        current_tool = parameters["Current_tool"]
        current_comment = parameters["Current_comment"]

        for tape_line in tape_lines[0]:
            if tape_line != "":
                self.tape1_list.append(
                    (config_line, tape_line, current_tool, current_comment)
                )
        for tape_line in tape_lines[1]:
            if tape_line != "":
                self.tape2_list.append(
                    (config_line, tape_line, current_tool, current_comment)
                )

    def get_parameters(self) -> dict:
        """Obtiene los parámetros actuales de configuración

        Returns:
            dict: Diccionario de parámetros
        """

        return {
            "Config_line": self.current_config_line,
            "Current_tool": self.current_tool,
            "Current_comment": self.current_comment,
        }

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

        self.config_widget.itemDoubleClicked.connect(self.item_modifier)
        self.tape1_widget.itemDoubleClicked.connect(self.item_modifier)
        self.tape2_widget.itemDoubleClicked.connect(self.item_modifier)

        self.config_widget.itemSelectionChanged.connect(self.config_selected)
        self.tape1_widget.itemSelectionChanged.connect(self.tape1_selected)
        self.tape2_widget.itemSelectionChanged.connect(self.tape2_selected)

    def update_config_widget(self) -> None:
        """Actualiza los datos en el widget de configuración"""

        config_lines = self.config_list
        self.config_widget.setRowCount(len(config_lines))
        for num, line in enumerate(config_lines):
            task_name = line[0]
            self.config_widget.setItem(num, 0, QTableWidgetItem(task_name))

    def update_tape_widget(self, widget: QTableWidget, tape: list):
        """Actualiza los datos en el widget de tape"""

        widget.setRowCount(len(tape))
        for num, line in enumerate(tape):
            widget.setItem(num, 0, QTableWidgetItem(line[1]))

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

                self.update_tape1_widget_selection()
                self.update_tape2_widget_selection()

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

    def item_modifier(self) -> None:
        """Obtiene la línea de configuración a modificar"""

        line = self.current_selection
        task = self.config_list[line[0]][0]
        data = self.config_list[line[0]][1]

        task_class = get_task_class(task)
        self.subtask1 = task_class(window)
        self.subtask1.modifier(data)

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
