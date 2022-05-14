from PySide6.QtWidgets import QMainWindow

from tools.subwindows_tools import key_pressed
from interfaces.ui_version import Ui_frm_version


class Version(QMainWindow, Ui_frm_version):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def keyPressEvent(self, qKeyEvent) -> None:
        key_pressed(self, qKeyEvent)