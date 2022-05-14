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
from subtasks.generators.misc_gen import misc_gen
from interfaces.ui_misc import Ui_frm_misc


class Misc(Subtask, Ui_frm_misc):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = subtasks_tools.tasks_list["Misc"]["Description"]
        self.image = "misc.png"

        self.cbx_stp.addItems(program_stops_list)
        self.cbx_chk.addItems(collet_operations_list)
        self.cbx_col.addItems(coolant_operations_list)
        self.cbx_sde.addItems(tape_sides_list)
        self.cbx_sde.setCurrentText(self.window.current_side)

    def collector(self) -> None:
        """Recolecta los datos de la subtarea ingresados por el usuario"""

        data = {
            "Com": self.tbx_com.text(),
            "Stp": self.cbx_stp.currentText(),
            "Chk": self.cbx_chk.currentText(),
            "Col": self.cbx_col.currentText(),
            "Sde": self.cbx_sde.currentText(),
            "Blk": False,
        }

        self.validator(data)

    def validator(self, data: dict) -> None:
        """Valida los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        if all_empty(data):
            all_blank_data_error(self)
            return
        self.converter(data)

    def converter(self, data: dict) -> None:
        """Formatea los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

        try:
            data["Com"] = ftext(data["Com"]) if data["Com"] != "" else ""

        except ValueError:
            data_type_error(self)
            return

        self.packer(data)

    def packer(self, data: dict) -> None:
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

        return misc_gen(machine, data)

    def modifier(self, data: dict) -> None:
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        self.modification = True
        com, stp, chk, col, sde, blk = data.values()

        self.tbx_com.setText(str(com))
        self.tbx_com.setSelection(0, 100)
        self.cbx_stp.setCurrentText(str(stp))
        self.cbx_chk.setCurrentText(str(chk))
        self.cbx_col.setCurrentText(str(col))
        self.cbx_sde.setCurrentText(str(sde))
        self.btn_save.setText("Actualizar")
        self.show()

    def processor(self, window: QMainWindow, data: dict) -> None:
        """Procesa los datos de configuración para cambiar valores de variables

        Args:
            window (QMainWindow): Clase principal de la aplicación
            data (dict): Diccionario de datos de configuración
        """

        window.save_required = True
        window.current_side = data["Sde"]

    def switcher(self, window: QMainWindow, data: dict):
        """Cambia el estado de los botones según los datos de configuración

        Args:
            window (QMainWindow): Clase principal de la aplicación
            data (dict): Diccionario de datos de configuración
        """

        pass