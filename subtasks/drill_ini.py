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

from subtasks.generators.drill_ini_gen import drill_ini_gen


class Drill_ini(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = sub_tasks.tasks_list["Drill_ini"]["Description"]
        self.modification = False

    def collector(self):
        """Recolecta los datos de la sub tarea ingresados por el usuario"""

        data = {
            "Blk": False,
        }

        self.validator(data)

    def validator(self, data: dict):
        """Valida los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

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
        data3 = prefab_center_drill_tool_call(21, 0, 0, -0.05, "$1")
        data4 = prefab_comment("AGUJERO CENTRO", "$1")
        data5 = prefab_center_drill(0.05, 0.003)
        data6 = prefab_tool_close(
            self.window.current_tool,
            self.window.current_side,
            self.window.current_bar_diameter,
        )
        data7 = prefab_drill_end()

        if self.modification:
            self.data_pack = [data1]
        else:
            self.data_pack = [
                data1,
                data2,
                data3,
                data4,
                data5,
                data6,
                data2,
                data7,
            ]

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

        return drill_ini_gen(machine, data)

    def modifier(self, data: dict):
        """Modifica la l??nea de configuraci??n seleccionada

        Args:
            data (dict): Diccionario de datos de configuraci??n
        """

        pass

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

        window.btn_drill_ini.setEnabled(False)
