from tools.constants import *
from PySide6.QtWidgets import QMainWindow


def load_persistent_data(window: QMainWindow):
    """Carga datos persistentes

    Args:
        window (QMainWindow): Ventana principal
    """

    window.current_machine = ""
    window.current_folder = ROOT_DIR


def load_default_tape_conditions(window: QMainWindow):
    """Cargar condiciones del tape

    Args:
        window (QMainWindow): Ventana principal
    """

    window.modified_task = False
    window.save_required = False


def load_default_data_lists(window: QMainWindow):
    """Carga los valores por defecto de las listas

    Args:
        window (QMainWindow): Ventana principal
    """

    window.config_list = []
    window.tape1_list = []
    window.tape2_list = []
    window.current_selection = []


def load_default_variables(window: QMainWindow):
    """Carga los valores por defecto de las variables principales

    Args:
        window (QMainWindow): Ventana principal
    """

    window.subtask1 = None
    window.current_widget = None
    window.config_file_name = ""
    window.file_extension = ""
    window.current_config_line = 0
    window.current_tool = 0
    window.current_comment = ""


def load_default_machining_data(window: QMainWindow):
    """Carga los valores por defecto de datos de mecanizado

    Args:
        window (QMainWindow): Ventana principal
    """

    window.current_comment = ""
    window.current_side = ""
    window.current_work_offset = ""
    window.part_name = ""
    window.main_tape_number = ""
    window.tape_description = ""

    window.current_bar_diameter = 0
    window.current_part_lenght = 0
    window.current_chuck_position = 0
    window.current_cutoff_tool = ""
    window.current_tool = 0
    window.current_tool_type = ""
    window.current_tool_diameter = 0
    window.current_tool_specification = ""
    window.swiss_back_machining = False
    window.main_tape_active = False
    window.platter_data = []

    window.first_tool_number = None
    window.first_tool_type = None
    window.first_tool_diameter = None
    window.first_tool_spec = None
    window.first_xps = None
    window.first_yps = None
    window.first_zps = None


def load_default_subrutine_data(window: QMainWindow):
    """Carga los valores por defecto de datos de subrutina

    Args:
        window (QMainWindow): Ventana principal
    """

    window.current_subrutine = 0
    window.current_main_program = ""
    window.platter_data = []
    window.subrutine_tool = 0
    window.subrutine_tool_diameter = 0
    window.subrutine_comment = ""
    window.last_subrutine_number = 3999
    window.subrutine_machine = ""
    window.subrutine_folder = ""


def load_default_window_components(window: QMainWindow):
    """Carga el estado por defecto de componentes de la ventana principal

    Args:
        window (QMainWindow): Ventana principal
    """

    window.window_components = {
        window.dock_functions: True,
        window.tape1_widget: True,
        window.tape2_widget: True,
        window.config_widget: True,
    }
