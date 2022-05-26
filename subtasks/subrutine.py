from PySide6.QtWidgets import QMainWindow

from main import *
from tools import subtasks
from tools.formatting import *
from tools.config_list import *
from tools.validations import *
from tools.directories import *
from tools.main_window import *
from tools.default_data import *
from tools.message_boxes import *
from tools.prefab_blocks import *
from tools.combobox_lists import *
from tools.file_management import *

from subtasks.subtask import Subtask
from subtasks.generators.subrutine_gen import subrutine_gen
from interfaces.ui_subrutine import Ui_frm_subrutine


class Subrutine(Subtask, Ui_frm_subrutine):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = subtasks.tasks_list["Subrutine"]["Description"]
        self.image = "subrutine.png"

        self.tbx_sub.setText(str(self.window.last_subrutine_number + 1))
        self.tbx_sub.setSelection(0, 100)

    def collector(self):
        """Recolecta los datos de la subtarea ingresados por el usuario"""

        data = {
            "Sub": self.tbx_sub.text(),
            "Rep": self.tbx_rep.text(),
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

        try:
            data["Sub"] = int(data["Sub"]) if data["Sub"] != "" else ""
            data["Rep"] = foper(data["Rep"])
        except ValueError:
            data_type_error(self)
            return

        self.packer(data)

    def packer(self, data: dict):
        """Agrega datos al paquete de datos a exportar

        Args:
            data (dict): Diccionario de datos recopilados
        """

        data1 = (self.task, data)
        self.data_pack = [data1]
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

        return subrutine_gen(machine, data)

    def modifier(self, data: dict):
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        self.modification = True
        sub, rep, blk = data.values()

        self.tbx_sub.setText(str(sub))
        self.tbx_sub.setSelection(0, 100)
        self.tbx_rep.setText(str(rep))
        self.btn_save.setText("Actualizar")
        self.show()

    def processor(self, window: QMainWindow, data: dict):
        """Procesa los datos de configuración para cambiar valores de variables

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """

        window.save_required = True
        window.current_side = "PRINCIPAL"
        window.last_subrutine_number = data["Sub"]

    def switcher(self, window: QMainWindow, data: dict):
        """Cambia el estado de los botones según los datos de configuración

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuración
        """

        pass
