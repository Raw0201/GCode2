from tools import subtasks_tools
from subtasks.subtask import Subtask
from tools.combo_lists import *
from tools.format_tools import *
from tools.validation_tools import *
from tools.message_boxes import *

from interfaces.ui_header import Ui_frm_header


class Collect(Subtask, Ui_frm_header):
    def __init__(self, main_window):
        super().__init__()
        self.task = subtasks_tools.tasks_list["Header"]["Description"]
        self.image = "header.png"
