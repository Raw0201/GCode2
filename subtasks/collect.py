from PySide6.QtWidgets import QMainWindow

from main import *
from tools import sub_tasks
from tools.formatting import *
from tools.config_list import *
from tools.validations import *
from tools.directories import *
from tools.main_window import *
from tools.default_data import *
from tools.message_boxes import *
from tools.prefab_blocks import *
from tools.combo_box_lists import *
from tools.file_management import *

from subtasks.sub_task import Subtask
from subtasks.generators.collect_gen import collect_gen
from interfaces.ui_collect import Ui_frm_collect


class Collect(Subtask, Ui_frm_collect):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = sub_tasks.tasks_list["Collect"]["Description"]
        self.image = "collect.png"

        self.cbx_clt.addItems(collect_modes)

    def collector(self):
        """Recolecta los datos de la sub tarea ingresados por el usuario"""

        data = {
            "Clt": self.cbx_clt.currentText(),
            "Chk": self.window.current_chuck_position,
            "Blk": False,
        }

        self.validator(data)

    def validator(self, data: dict):
        """Valida los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        if any_empty(data):
            blank_data_error(self)
            return
        self.converter(data)

    def converter(self, data: dict):
        """Formatea los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        self.packer(data)

    def packer(self, data: dict):
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
        """Genera la lista de l??neas de tape

        Args:
            machine (str): M??quina actual
            data (dict): Diccionario de datos de configuraci??n

        Returns:
            list: Lista de l??neas de tape
        """

        data["Chk"] = self.current_chuck_position

        return collect_gen(machine, data)

    def modifier(self, data: dict):
        """Modifica la l??nea de configuraci??n seleccionada

        Args:
            data (dict): Diccionario de datos de configuraci??n
        """

        self.modification = True
        clt, chk, blk = data.values()

        self.cbx_clt.setCurrentText(str(clt))
        self.btn_save.setText("Actualizar")
        self.show()

    def processor(self, window: QMainWindow, data: dict):
        """Procesa los datos de configuraci??n para cambiar valores de variables

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuraci??n
        """

        window.save_required = True

    def switcher(self, window: QMainWindow, data: dict):
        """Cambia el estado de los botones seg??n los datos de configuraci??n

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuraci??n
        """

        window.btn_collect.setEnabled(False)
