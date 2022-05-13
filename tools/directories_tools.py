import contextlib
import os

from tools.constants import *


def create_machine_folders():
    root = ROOT_DIR
    machines = MACHINES

    with contextlib.suppress(FileExistsError):
        os.mkdir(root)
    os.chdir(root)

    with contextlib.suppress(FileExistsError):
        for machine in machines:
            os.mkdir(machine)


def update_file_dir(window) -> None:
    """Actualiza el forder de guardado"""

    root = ROOT_DIR
    window.current_folder = f"{root}/{window.current_machine}"
    os.chdir(window.current_folder)
