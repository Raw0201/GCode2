from PySide6.QtWidgets import QMainWindow
from main import *

from tools import subtasks_tools
from tools.combo_lists import *
from tools.format_tools import *
from tools.message_boxes import *
from tools.validation_tools import *
from tools.default_data_tools import *
from tools.config_list_tools import *
from tools.file_tools import *
from tools.directories_tools import *
from tools.main_window_tools import *
from subtasks.subtask import Subtask

from subtasks.generators.header_gen import header_gen
from interfaces.ui_header import Ui_frm_header


class Header(Subtask, Ui_frm_header):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = subtasks_tools.tasks_list["Header"]["Description"]
        self.image = "header.png"

        self.cbx_mch.addItems(machines_list)
        self.cbx_cof.addItems(cutoff_list)
        self.cbx_wrk.addItems(work_offset_list)

    def collector(self) -> None:
        """Recolecta los datos de la subtarea ingresados por el usuario"""

        data = {
            "Prt": self.tbx_prt.text(),
            "Pgr": self.tbx_pgr.text(),
            "Dsc": self.tbx_dsc.text(),
            "Mch": self.cbx_mch.currentText(),
            "Dia": self.tbx_dia.text(),
            "Lgt": self.tbx_lgt.text(),
            "Chk": self.tbx_chk.text(),
            "Cof": self.cbx_cof.currentText(),
            "Wrk": self.cbx_wrk.currentText(),
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

        try:
            data["Prt"] = ftext(data["Prt"]) if data["Prt"] != "" else ""
            data["Pgr"] = ftext(data["Pgr"]) if data["Pgr"] != "" else ""
            data["Dsc"] = ftext(data["Dsc"]) if data["Dsc"] != "" else ""
            data["Dia"] = foper(data["Dia"])
            data["Lgt"] = foper(data["Lgt"])
            data["Chk"] = foper(data["Chk"])

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

        return header_gen(machine, data)

    def modifier(self, data: dict) -> None:
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        self.modification = True
        prt, pgr, dsc, mch, dia, lgt, chk, cof, wrk = data.values()

        self.tbx_prt.setText(str(prt))
        self.tbx_prt.setSelection(0, 100)
        self.tbx_pgr.setText(str(pgr))
        self.tbx_dsc.setText(str(dsc))
        self.cbx_mch.setCurrentText(str(mch))
        self.tbx_dia.setText(str(dia))
        self.tbx_lgt.setText(str(lgt))
        self.tbx_chk.setText(str(chk))
        self.cbx_cof.setCurrentText(str(cof))
        self.cbx_wrk.setCurrentText(str(wrk))
        self.btn_save.setText("Actualizar")
        self.show()

    def processor(self, window: QMainWindow, data: dict) -> None:
        """Procesa los datos de configuración para cambiar valores de variables

        Args:
            window (QMainWindow): Clase principal de la aplicación
            data (dict): Diccionario de datos de configuración
        """

        window.save_required = True
        window.current_machine = data["Mch"]
        window.main_tape_active = True
        window.current_side = "$1"
        window.current_machine = data["Mch"]
        window.part_name = data["Prt"]
        window.main_tape_number = data["Pgr"]
        window.tape_description = data["Dsc"]
        window.current_bar_diameter = data["Dia"]
        window.current_part_lenght = data["Lgt"]
        window.current_chuck_position = data["Chk"]
        window.current_cutoff_tool = data["Cof"]
        window.current_work_offset = data["Wrk"]
        window.swiss_back_machining = data["Chk"] > 0

        update_file_name(window)
        update_file_dir(window)
        load_main_title(window)

    def switcher(self, window: QMainWindow, data: dict):
        """Cambia el estado de los botones según los datos de configuración

        Args:
            window (QMainWindow): Clase principal de la aplicación
            data (dict): Diccionario de datos de configuración
        """

        load_default_buttons_status(window)
        load_default_tape_conditions(window)

        for button_list in (
            window.program_buttons_list,
            window.tool_buttons_list,
            window.machine_buttons_list,
            window.turning_buttons_list,
            window.milling_buttons_list,
            window.milling_cycle_buttons_list,
            window.drilling_buttons_list,
        ):
            for button in button_list:
                button.setEnabled(True)

        if window.current_machine != "Mazak":
            for button in window.plate_buttons_list:
                button.setEnabled(False)

        if window.current_machine == "Mazak":
            for button in window.turning_buttons_list:
                button.setEnabled(False)

        window.btn_header.setEnabled(False)
        window.btn_tool_close.setEnabled(False)
        # window.btn_collect.setEnabled(False)

        end_enabled = not window.main_tape_active
        window.btn_end.setEnabled(end_enabled)
