import contextlib
import os

from tools.constants import *


class Config_folders:
    def __init__(self) -> None:
        self.root = ROOT_DIR
        self.machines = MACHINES

    def create_machine_folders(self) -> None:
        with contextlib.suppress(FileExistsError):
            os.mkdir(self.root)
        os.chdir(self.root)

        with contextlib.suppress(FileExistsError):
            for machine in self.machines:
                os.mkdir(machine)
