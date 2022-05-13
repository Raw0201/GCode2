import tools
from tools.default_data_tools import *
from tools.widgets_tools import *
from tools.tape_lists_tools import *


def collect_data(window, data_class: str):
    """Crea una subtarea para recolectar datos de configuración

    Args:
        data_class (str): Clase de la subtarea
    """

    subtask_class = tools.subtasks_tools.tasks_list[data_class]["Name"]
    window.subtask1 = subtask_class(window)

    if data_class not in {"Free"}:
        window.subtask1.show()
    else:
        window.subtask1.collector()


def store_config_data(window, data_pack: list, modification: bool):
    """Almacena los datos recolectados en la lista de configuración

    Args:
        data_pack (list): Lista de datos recolectados
        modification (bool): Indicador de datos modificados
    """

    if modification:
        update_modified_data(window, data_pack)
    elif not window.current_selection:
        append_new_data(window, data_pack)
    else:
        insert_new_data(window, data_pack)

    load_default_variables(window)
    generate_tape_lines(window, window.config_list)
    update_data_widgets(window)


def update_modified_data(window, data_pack: list):
    """Actualiza los datos modificados en la lista de configuración

    Args:
        data_pack (list): Paquete de datos modificados
    """

    task = data_pack[0][0]
    data = data_pack[0][1]
    index = window.current_selection[0]
    window.config_list[index] = [task, data]


def append_new_data(window, data_pack: list):
    """Agrega los datos recolectados al final de la lista

    Args:
        data_pack (list): Paquete de datos recolectados
    """

    for pack in data_pack:
        task = pack[0]
        data = pack[1]
        window.config_list.append([task, data])

        end_line = len(window.config_list) - 1
        window.current_selection = [end_line]


def insert_new_data(window, data_pack: list):
    """Inserta los datos recolectados en una posición de la lista

    Args:
        data_pack (list): Paquete de datos recolectados
    """

    for pack in data_pack:
        task = pack[0]
        data = pack[1]
        current_index = window.current_selection[0] + 1
        window.config_list.insert(current_index, [task, data])
        window.current_selection = [current_index]
