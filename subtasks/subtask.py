from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow

from tools.subtasks_tools import image_load, key_pressed
from subtasks.helper import Helper


class Subtask(QMainWindow):
    collected_data_signal = Signal()
    updated_data_signal = Signal()

    def __init__(self):
        super().__init__()
        self.helper1 = Helper()
        self.setupUi(self)
        self.move(0, 0)

        self.data_pack = None
        self.modified_data = False
        self.btn_save.clicked.connect(self.collector)

        self.image = ""
        self.btn_help.clicked.connect(lambda: self.helper(self.image))

    def collector(self):
        pass

    def helper(self, image):
        self.helper1.show()
        image_load(self.helper1.lbl_image, image)

    def keyPressEvent(self, qKeyEvent) -> None:
        key_pressed(self, qKeyEvent)

    def closeEvent(self, event):
        self.close()
