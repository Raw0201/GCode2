from PySide6.QtWidgets import QMainWindow

from main import *
from tools import subtasks_tools
from tools.file_tools import *
from tools.combo_lists import *
from tools.format_tools import *
from tools.config_tools import *
from tools.message_boxes import *
from tools.prefab_blocks import *
from tools.validation_tools import *
from tools.directories_tools import *
from tools.main_window_tools import *
from tools.default_data_tools import *

from subtasks.subtask import Subtask
from subtasks.generators.collect_gen import collect_gen
from interfaces.ui_collect import Ui_frm_collect


class Collect(Subtask, Ui_frm_collect):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = subtasks_tools.tasks_list["Collect"]["Description"]
        self.image = "collect.png"

        self.cbx_clt.addItems(collect_modes)

    def collector(self) -> None:
        """Recolecta los datos de la subtarea ingresados por el usuario"""

        data = {
            "Clt": self.cbx_clt.currentText(),
            "Chk": self.window.current_chuck_position,
            "Blk": False,
        }

        self.validator(data)

    def validator(self, data: dict) -> None:
        """Valida los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        if any_empty(data):
            blank_data_error(self)
            return
        self.converter(data)

    def converter(self, data: dict) -> None:
        """Formatea los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        self.packer(data)

    def packer(self, data: dict) -> None:
        """Agrega datos al paquete de datos a exportar

        Args:
            data (dict): Diccionario de datos recopilados
        """

        data1 = (self.task, data)
        data2 = prefab_space()
        self.data_pack = [data2, data1]
        store_config_data(
            self.window,
            self.data_pack,
            self.modification,
        )

        self.close()
        self.modification = False

    def generator(self, machine: str, data: dict) -> list:
        """Genera la lista de líneas de tape

        Args:
            machine (str): Máquina actual
            data (dict): Diccionario de datos de configuración

        Returns:
            list: Lista de líneas de tape
        """

        data["Chk"] = self.current_chuck_position

        return collect_gen(machine, data)

    def modifier(self, data: dict) -> None:
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        self.modification = True
        clt, chk, blk = data.values()

        self.cbx_clt.setCurrentText(str(clt))
        self.btn_save.setText("Actualizar")
        self.show()

    def processor(self, window: QMainWindow, data: dict) -> None:
        """Procesa los datos de configuración para cambiar valores de variables

        Args:
            window (QMainWindow): Clase principal de la aplicación
            data (dict): Diccionario de datos de configuración
        """

        window.save_required = True

    def switcher(self, window: QMainWindow, data: dict):
        """Cambia el estado de los botones según los datos de configuración

        Args:
            window (QMainWindow): Clase principal de la aplicación
            data (dict): Diccionario de datos de configuración
        """

        window.btn_collect.setEnabled(False)
