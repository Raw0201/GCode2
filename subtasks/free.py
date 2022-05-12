from PySide6.QtWidgets import QMainWindow

from tools import subtasks_list
from tools.combo_lists import *
from tools.format_tools import *
from tools.message_boxes import *
from tools.validation_tools import *
from subtasks.generators.free_gen import free_gen


class Free(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.task = subtasks_list.tasks_list["Free"]["Description"]
        self.image = "free.png"
        self.modification = False

    def collector(self) -> None:
        """Recolecta los datos de la subtarea ingresados por el usuario"""

        data = {
            "Fre": "  ",
        }

        self.validator(data)

    def validator(self, data: dict) -> None:
        """Valida los datos del diccionario recopilado

        Args:
            data (dict): Diccionario de datos recopilados
        """

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
        self.data_pack = [data1]

        self.main_window.store_config_data(
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

        return free_gen(machine, data)

    def modifier(self, data: dict) -> None:
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        pass

    def processor(self, main_window: QMainWindow, data: dict) -> None:
        """Procesa los datos de configuración para cambiar valores de variables

        Args:
            main_window (QMainWindow): Clase principal de la aplicación
            data (dict): Diccionario de datos de configuración
        """

        pass

    def switcher(self, main_window: QMainWindow, data: dict):
        """Cambia el estado de los botones según los datos de configuración

        Args:
            main_window (QMainWindow): Clase principal de la aplicación
            data (dict): Diccionario de datos de configuración
        """

        pass
