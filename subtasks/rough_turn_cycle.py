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
from subtasks.generators.rough_turn_cycle_gen import rough_turn_cycle_gen
from interfaces.ui_rough_turn_cycle import Ui_frm_rough_turn_cycle


class Rough_turn_cycle(Subtask, Ui_frm_rough_turn_cycle):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = sub_tasks.tasks_list["Rough_turn_cycle"]["Description"]
        self.image = "rough_turn_cycle.png"

    def collector(self):
        """Recolecta los datos de la sub tarea ingresados por el usuario"""

        data = {
            "Seq": self.tbx_seq.text(),
            "Cut": self.tbx_cut.text(),
            "Ovr": self.tbx_ovr.text(),
            "Fed": self.tbx_fed.text(),
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
            data["Seq"] = foper(data["Seq"])
            data["Cut"] = foper(data["Cut"])
            data["Ovr"] = foper(data["Ovr"])
            data["Fed"] = foper(data["Fed"])

        except ValueError:
            data_type_error(self)
            return

        self.packer(data)

    def packer(self, data: dict):
        """Agrega datos al paquete de datos a exportar

        Args:
            data (dict): Diccionario de datos recopilados
        """

        machine = self.window.current_machine
        sequence = int(data["Seq"])
        self.window.current_sequence_number = sequence

        data1 = (self.task, data)
        data2 = [
            "        Torneado lineal",
            {
                "Xin": 0.0,
                "Zin": "",
                "Fed": "",
                "Seq": sequence,
                "Mov": "RAPIDO",
                "Sde": "$1",
                "Blk": False,
            },
        ]
        data3 = [
            "        Torneado lineal",
            {
                "Xin": 0.0,
                "Zin": "",
                "Fed": "",
                "Seq": sequence + 100,
                "Mov": "RAPIDO",
                "Sde": "$1",
                "Blk": False,
            },
        ]
        data4 = [
            "        Finalizar ciclo de torneado desbaste",
            {
                "Blk": False,
            },
        ]

        self.data_pack = (
            [data1, data2, data3] if machine != "OMNITURN" else [data1, data4]
        )
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

        return rough_turn_cycle_gen(machine, data)

    def modifier(self, data: dict):
        """Modifica la l??nea de configuraci??n seleccionada

        Args:
            data (dict): Diccionario de datos de configuraci??n
        """

        self.modification = True
        seq, cut, ovr, fed, blk = data.values()

        self.tbx_seq.setText(str(seq))
        self.tbx_seq.setSelection(0, 100)
        self.tbx_cut.setText(str(cut))
        self.tbx_ovr.setText(str(ovr))
        self.tbx_fed.setText(str(fed))
        self.btn_save.setText("Actualizar")
        self.show()

    def processor(self, window: QMainWindow, data: dict):
        """Procesa los datos de configuraci??n para cambiar valores de variables

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuraci??n
        """

        window.save_required = True
        window.current_sequence_number = int(data["Seq"])

    def switcher(self, window: QMainWindow, data: dict):
        """Cambia el estado de los botones seg??n los datos de configuraci??n

        Args:
            window (QMainWindow): Ventana principal
            data (dict): Diccionario de datos de configuraci??n
        """

        window.btn_rough_turn_cycle.setEnabled(True)

        if window.current_machine == "OMNITURN":
            window.btn_rough_turn_cycle_end.setEnabled(True)
        else:
            window.btn_rough_turn_cycle_end.setEnabled(False)
