from tools import subtasks_list
from subtasks.subtask import Subtask
from tools.combo_lists import *
from tools.format_tools import *
from tools.validation_tools import *
from tools.message_boxes import *

from interfaces.ui_header import Ui_frm_header


class Header(Subtask, Ui_frm_header):
    def __init__(self):
        super().__init__()
        self.task = subtasks_list.tasks_list["Header"]["Description"]
        self.image = "header.png"

        self.cbx_mch.addItems(machines_list)
        self.cbx_cof.addItems(cutoff_list)
        self.cbx_wrk.addItems(work_offset_list)

    def collector(self) -> None:

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
        if any_empty(data):
            blank_data_error(self)
            return
        self.converter(data)

    def converter(self, data: dict) -> None:
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
        data1 = (self.task, data)
        self.data_pack = [data1]
        self.collected_data_signal.emit()
        self.close()
        self.modified_data = False

    def generator(self, data: dict) -> None:
        pass
        # parameters = window.get_parameters()
        # machine = window.current_machine
        # lines = header_gen(machine, data)
        # window.tape_generator(lines, parameters)

    def modifier(self, data: dict) -> None:
        self.modified_data = True
        # prt, pgr, dsc, mch, dia, lgt, chk, cof, wrk = data.values()

        # self.subtask1 = Header()
        # self.subtask1.tbx_prt.setText(str(prt))
        # self.subtask1.tbx_prt.setSelection(0, 100)
        # self.subtask1.tbx_pgr.setText(str(pgr))
        # self.subtask1.tbx_dsc.setText(str(dsc))
        # self.subtask1.cbx_mch.setCurrentText(str(mch))
        # self.subtask1.tbx_dia.setText(str(dia))
        # self.subtask1.tbx_lgt.setText(str(lgt))
        # self.subtask1.tbx_chk.setText(str(chk))
        # self.subtask1.cbx_cof.setCurrentText(str(cof))
        # self.subtask1.cbx_wrk.setCurrentText(str(wrk))
        # self.subtask1.btn_save.setText("Actualizar")
        # self.subtask1.show()

    def processor(self, data: dict) -> None:
        pass

    def button_switcher(self, main_window) -> None:

        for button in main_window.main_buttons_list:
            button.setEnabled(False)
