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
from subtasks.generators.tool_call_gen import tool_call_gen
from interfaces.ui_tool_call import Ui_frm_tool_call


class Tool_call(Subtask, Ui_frm_tool_call):
    def __init__(self, main_window):
        super().__init__()
        self.window = main_window
        self.task = subtasks_tools.tasks_list["Tool_call"]["Description"]
        self.image = "tool_call.png"

        self.cbx_typ.addItems(tool_list)
        self.cbx_sde.addItems(tape_sides_list)
        self.cbx_sde.setCurrentText(self.window.current_side)

    def collector(self) -> None:
        """Recolecta los datos de la subtarea ingresados por el usuario"""

        data = {
            "Tol": self.tbx_tol.text(),
            "Typ": self.cbx_typ.currentText(),
            "Dia": self.tbx_dia.text(),
            "Spc": self.tbx_spc.text(),
            "Sde": self.cbx_sde.currentText(),
            "Xin": self.tbx_xin.text(),
            "Yin": self.tbx_yin.text(),
            "Zin": self.tbx_zin.text(),
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

        try:
            data["Tol"] = int(data["Tol"])
            data["Dia"] = foper(data["Dia"])
            data["Spc"] = ftext(data["Spc"]) if data["Spc"] != "" else ""
            data["Xin"] = foper(data["Xin"])
            data["Yin"] = foper(data["Yin"])
            data["Zin"] = foper(data["Zin"])
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
        data2 = prefab_space()
        data3 = prefab_spindle(
            3000,
            "NORMAL",
            data["Sde"],
        )
        data4 = prefab_comment(
            "DESCRIPCION",
            data["Sde"],
        )
        data5 = prefab_tool_close(
            data["Tol"],
            data["Sde"],
            self.window.current_bar_diameter,
        )

        machine = self.window.current_machine
        if self.modification:
            self.data_pack = [data1]
        elif machine in ("B12", "A16", "K16", "E16", "OMNITURN"):
            self.data_pack = [data2, data1, data4, data5]
        else:
            self.data_pack = [data2, data1, data3, data4, data5]

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

        return tool_call_gen(machine, data)

    def modifier(self, data: dict) -> None:
        """Modifica la línea de configuración seleccionada

        Args:
            data (dict): Diccionario de datos de configuración
        """

        self.modification = True
        tol, typ, dia, spc, sde, xin, yin, zin, blk = data.values()

        self.tbx_tol.setText(str(tol))
        self.tbx_tol.setSelection(0, 100)
        self.cbx_typ.setCurrentText(str(typ))
        self.tbx_dia.setText(str(dia))
        self.tbx_spc.setText(str(spc))
        self.cbx_sde.setCurrentText(str(sde))
        self.tbx_xin.setText(str(xin))
        self.tbx_yin.setText(str(yin))
        self.tbx_zin.setText(str(zin))
        self.btn_save.setText("Actualizar")
        self.show()

    def processor(self, window: QMainWindow, data: dict) -> None:
        """Procesa los datos de configuración para cambiar valores de variables

        Args:
            window (QMainWindow): Clase principal de la aplicación
            data (dict): Diccionario de datos de configuración
        """

        window.save_required = True
        window.current_tool = int(data["Tol"])
        window.current_side = data["Sde"]

        window.first_tool_number = (
            data["Tol"]
            if window.first_tool_number is None
            else window.first_tool_number
        )
        window.first_tool_type = (
            data["Typ"]
            if window.first_tool_type is None
            else window.first_tool_type
        )

        window.first_tool_diameter = (
            data["Dia"]
            if window.first_tool_diameter is None
            else window.first_tool_diameter
        )
        window.first_tool_spec = (
            data["Spc"]
            if window.first_tool_spec is None
            else window.first_tool_spec
        )
        window.first_xps = (
            data["Xin"] if window.first_xps is None else window.first_xps
        )
        window.first_yps = (
            data["Yin"] if window.first_yps is None else window.first_yps
        )
        window.first_zps = (
            data["Zin"] if window.first_zps is None else window.first_zps
        )

    def switcher(self, window: QMainWindow, data: dict):
        """Cambia el estado de los botones según los datos de configuración

        Args:
            window (QMainWindow): Clase principal de la aplicación
            data (dict): Diccionario de datos de configuración
        """

        window.btn_tool_call.setEnabled(True)
        window.btn_tool_close.setEnabled(True)
        window.btn_end.setEnabled(True)
