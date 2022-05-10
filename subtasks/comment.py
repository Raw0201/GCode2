from tools import subtasks_list
from subtasks.subtask import Subtask
from tools.combo_lists import *
from tools.format_tools import *
from tools.validation_tools import *
from tools.message_boxes import *

from interfaces.ui_header import Ui_frm_header


class Comment(Subtask, Ui_frm_header):
    def __init__(self):
        super().__init__()
        self.task = subtasks_list.tasks_list["Header"]["Description"]
        self.image = "header.png"
