from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from pathlib import Path

from PySide6.QtWidgets import QLabel


def key_pressed(self, qKeyEvent) -> None:
    if qKeyEvent.key() in [
        QtCore.Qt.Key_Return,
        QtCore.Qt.Key_Enter,
        QtCore.Qt.Key_Down,
    ]:
        self.focusNextChild()
    if qKeyEvent.key() == QtCore.Qt.Key_Up:
        self.focusPreviousChild()
    elif qKeyEvent.key() == QtCore.Qt.Key_Escape:
        self.modified_task = False
        self.close()
    elif qKeyEvent.modifiers() == QtCore.Qt.ControlModifier:
        if qKeyEvent.key() == QtCore.Qt.Key_S:
            self.collector()
    else:
        return


def abs_path(file: str) -> str:
    return str(Path(__file__).parent.absolute() / file)


def image_load(label: QLabel, image: str) -> None:
    image = QPixmap(abs_path(f"../resources/{image}"))
    label.setPixmap(image)
    label.setScaledContents(True)
