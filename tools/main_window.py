import contextlib
import os
import json
import tools

from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import QEvent

from tools.constants import *
from tools.formatting import *
from tools.prefab_blocks import prefab_comment, prefab_sub_header
from tools.tape_lists import *
from tools.config_list import *
from tools.directories import *
from tools.default_data import *
from tools.main_buttons import *
from tools.message_boxes import *
from tools.file_management import *


def load_main_title(window: QMainWindow):
    """Actualiza el título de la ventana

    Args:
        window (QMainWindow): Ventana principal
    """

    app_name = "G-Code Editor"
    machine_type = window.current_machine
    file_name = window.config_file_name
    file_extension = window.file_extension
    folder = window.current_folder
    folder = folder if folder == f"{ROOT_DIR}/" else f"{folder}/"
    file = f"{file_name}{file_extension}"
    tape_name = f"- {folder}{file} - " if file_name != "" else ""
    tape_description = f"{window.tape_description}"
    save_status = "*" if window.save_required else ""

    app_machine = f"{app_name} {machine_type}"
    tape_data = f"{tape_name} {tape_description}"
    main_title = f"{app_machine}  {tape_data} {save_status}"

    window.setWindowTitle(main_title)


def new_tape(window: QMainWindow):
    """Crear un nuevo tape

    Args:
        window (QMainWindow): Ventana principal
    """

    dialog = new_tape_question(window)
    if dialog == QMessageBox.Yes:
        create_new_tape(window)


def create_new_tape(window: QMainWindow):
    """Limpia los datos para iniciar un nuevo tape

    Args:
        window (QMainWindow): Ventana principal
    """

    load_default_data_lists(window)
    load_default_variables(window)
    load_default_tape_conditions(window)
    load_default_machining_data(window)
    tools.main_buttons.load_default_buttons_status(window)
    load_main_title(window)

    window.config_widget.clearContents()
    window.tape1_widget.clearContents()
    window.tape2_widget.clearContents()
    window.config_widget.setRowCount(0)
    window.tape1_widget.setRowCount(0)
    window.tape2_widget.setRowCount(0)


def open_file(window: QMainWindow):
    """Abrir un archivo de configuración

    Args:
        window (QMainWindow): Ventana principal
    """

    try:
        os.chdir(window.current_folder)
        file_name = QFileDialog.getOpenFileName(
            window,
            caption=("Abrir programa"),
            dir=window.current_folder,
            filter=("Archivos de configuración (*.json)"),
        )

        with open(file_name[0]) as file:
            window.config_list = json.load(file)

        window.current_folder = os.path.dirname(file_name[0])
        window.current_machine = window.config_list[0][1]["Mch"]
        os.chdir(window.current_folder)

        update_data(window)
        window.save_required = False
        load_main_title(window)

    except OSError:
        return
    except KeyError:
        file_open_error(window)
        window.create_new_tape()


def save_config(window: QMainWindow):
    """Guardar el archivo de configuración

    Args:
        window (QMainWindow): Ventana principal
    """

    if not window.tape1_list:
        return

    update_data(window)

    file = f"{window.config_file_name}.json"
    with open(file, "w") as file:
        json.dump(window.config_list, file)
    save_tape(window)


def save_tape(window: QMainWindow):
    """Guardar el archivo de configuración

    Args:
        window (QMainWindow): Ventana principal
    """

    if not window.tape1_list:
        return

    os.chdir(ROOT_DIR)
    complete_tape = make_tape(window)

    file = f"{window.config_file_name}{window.file_extension}"
    with open(file, "w") as tape:
        for lines in complete_tape:
            tape.write(lines + "\n")

    window.save_required = False
    load_main_title(window)
    os.chdir(window.current_folder)


def make_tape(window: QMainWindow) -> list:
    """Crea las líneas del tape

    Args:
        window (QMainWindow): Ventana principal

    Returns:
        list: Tape completo
    """

    tape = []
    blank_space = fspace()

    for line in window.tape1_list:
        data = line[1]
        if data != blank_space:
            tape.append(data)
    for line in window.tape2_list:
        data = line[1]
        if data != blank_space:
            tape.append(data)
    return tape


def close_app(window: QMainWindow, event: QEvent):
    """Evento de cierre de la ventana

    Args:
        window (QMainWindow): Ventana principal
        event (QEvent): Evento de cierre de ventana
    """

    result = QMessageBox.question(
        window,
        "Cerrar la aplicación",
        "Seguro que desea cerrar?",
        QMessageBox.Yes | QMessageBox.No,
    )
    event.ignore()

    if result == QMessageBox.Yes:
        if window.subtask1:
            window.subtask1.close()
        event.accept()


def close_action(window: QMainWindow):
    """Evento de cierre de la ventana

    Args:
        window (QMainWindow): Ventana principal
        event (QEvent): Evento de cierre de ventana
    """

    window.close()


def delete_lines(window: QMainWindow):
    """Borra las líneas seleccionadas

    Args:
        window (QMainWindow): Ventana principal
    """

    if not window.config_list or not window.current_selection:
        return

    if window.current_selection[0] == 0:
        dialog = delete_header_information(window)
        return

    dialog = delete_lines_warning(window)

    if dialog == QMessageBox.Yes:
        start = window.current_selection[0]
        end = window.current_selection[-1] + 1
        del window.config_list[start:end]
        update_data(window)


def duplicate_lines(window: QMainWindow):
    """Duplica las líneas seleccionadas

    Args:
        window (QMainWindow): Ventana principal
    """

    index_list = window.current_selection
    if index_list[0] == 0:
        duplicate_header_information(window)
        return

    duplicated_lines = [window.config_list[index] for index in index_list]
    insertion_index = index_list[-1] + 1
    for line in duplicated_lines:
        window.config_list.insert(insertion_index, line)
        insertion_index += 1

    selection_len = len(index_list)
    for n, index in enumerate(window.current_selection):
        window.current_selection[n] = index + selection_len

    update_data(window)


def movement(window: QMainWindow, direction: str):
    """Valida el movimiento de las líneas seleccionadas

    Args:
        window (QMainWindow): Ventana principal
        direction (str): Dirección del movimiento
    """

    index_list = window.current_selection

    down_limit = len(window.config_list) - 1
    if window.config_list[index_list[0]][0] in (
        "Inicio de programa",
        "Fin de programa",
    ):
        movement_error_information(window)
        return
    elif index_list[0] == 1 and direction == "up":
        movement_error_information(window)
        return
    elif index_list[-1] == down_limit and direction == "down":
        return

    move_lines(window, index_list, direction)


def move_lines(window: QMainWindow, index_list: list, direction: str):
    """Mueve las líneas de configuración

    Args:
        window (QMainWindow): Ventana principal
        index_list (list): Lista de índices a mover
        direction (str): Dirección del movimiento
    """

    moved_data = [window.config_list[index] for index in index_list]
    start, end = index_list[0], index_list[-1] + 1
    del window.config_list[start:end]

    increment = 1 if direction == "down" else -1
    index = start + increment
    for line in moved_data:
        window.config_list.insert(index, line)
        index += 1

    for n, index in enumerate(window.current_selection):
        window.current_selection[n] = index + increment

    update_data(window)


def param_mod(window: QMainWindow, param: str, direction: str, amount: float):
    """Modifica un parámetro en las líneas seleccionadas

    Args:
        window (QMainWindow): Ventana principal
        param (str): Parámetro a modificar
        direction (str): Dirección de la modificación
        amount (float): Dimensión de la modificación
    """

    mod = amount if direction == "up" else amount * -1

    if param in {"Sub", "Rep"}:
        mod = int(mod)
    elif window.current_machine == "OMNITURN" and param == "Fed":
        mod *= 1000

    index_list = window.current_selection
    for index in index_list:
        with contextlib.suppress(KeyError):
            modded = window.config_list[index][1][param]
            window.config_list[index][1][param] = modded + mod

    update_data(window)


def param_invert(window: QMainWindow, param: str):
    """Modifica un parámetro en las líneas seleccionadas

    Args:
        window (QMainWindow): Ventana principal
        param (str): Parámetro a invertir
    """

    mod = -1

    index_list = window.current_selection
    for index in index_list:
        with contextlib.suppress(KeyError):
            modded = window.config_list[index][1][param]
            window.config_list[index][1][param] = modded * mod

    update_data(window)


def side_changer(window: QMainWindow, side: str):
    """Modifica un parámetro en las líneas seleccionadas

    Args:
        window (QMainWindow): Ventana principal
        side (str): Lado a desplazar
    """

    index_list = window.current_selection
    for index in index_list:
        with contextlib.suppress(KeyError):
            modded = window.config_list[index][1]["Sde"]
            window.config_list[index][1]["Sde"] = side

    update_data(window)


def component_view(window: QMainWindow, component: object):
    """Muestra u oculta el componente seleccionado

    Args:
        window(QMainWindow): Ventana principal
        component (QtWidget): Componente a mostrar u ocultar
    """

    state = not window.window_components[component]

    if state:
        component.show()
    else:
        component.hide()

    window.window_components[component] = state


def home_position(window: QMainWindow):
    """Obtiene la línea inicial del programa

    Args:
        window (QMainWindow): Ventana principal
    """

    line = 0
    go_to_position(window, line)


def end_position(window: QMainWindow):
    """Obtiene la línea final del programa

    Args:
        window (QMainWindow): Ventana principal
    """

    line = len(window.config_list) - 1
    go_to_position(window, line)


def go_to_position(window: QMainWindow, line: list):
    """Ir a la línea indicada

    Args:
        window (QMainWindow): Ventana principal
        line (list): Línea a la que desplazarse
    """

    window.current_selection = [line]
    window.config_widget.setCurrentCell(line, 0)
    update_tape1_widget_selection(window)
    update_tape2_widget_selection(window)


def block_lines(window: QMainWindow):
    """Bloquea o desbloquea las líneas seleccionadas

    Args:
        window (QMainWindow): Ventana principal
    """

    index_list = window.current_selection
    for index in index_list:
        with contextlib.suppress(KeyError):
            block = window.config_list[index][1]["Blk"]
            window.config_list[index][1]["Blk"] = not block
    update_data(window)


def update_data(window: QMainWindow):
    """Actualiza pantalla después de abrir

    Args:
        window (QMainWindow): Ventana principal
    """

    load_default_machining_data(window)
    generate_tape_lines(window, window.config_list)
    update_config_widget(window)
    update_tape_widget(window.tape1_widget, window.tape1_list)
    update_tape_widget(window.tape2_widget, window.tape2_list)
    update_config_widget_selection(window)
    update_tape1_widget_selection(window)
    update_tape2_widget_selection(window)

    window.modified_task = False


def subrutine_prep(window: QMainWindow):
    """Verifica si se ha seleccionado una subrutina

    Args:
        window (QMainWindow): Ventana principal
    """

    index_list = window.current_selection
    index = index_list[0] if index_list else 0
    with contextlib.suppress(KeyError, IndexError):
        if window.config_list[index][1]["Sub"]:
            save_config(window)
            load_subrutine_data(window, index)
            search_subrutine(window)


def load_subrutine_data(window: QMainWindow, index: int):
    """Carga los datos para la subrutina

    Args:
        window (QMainWindow): Ventana principal
        index (int): Ubicación de la subrutina en la lista de tapes
    """

    window.current_subrutine = window.config_list[index][1]["Sub"]
    window.current_main_program = window.main_tape_number
    window.subrutine_machine = window.current_machine
    window.subrutine_folder = window.current_folder

    for line in window.tape1_list:
        window.subrutine_tool = line[2]
        window.subrutine_tool_type = line[3]
        window.subrutine_tool_diameter = line[4]
        window.subrutine_tool_specification = line[5]
        window.subrutine_comment = line[6]
        while line[0] == index:
            break


def search_subrutine(window: QMainWindow):
    """Busca o crea la subrutina

    Args:
        window (QMainWindow): Ventana principal
    """

    try:
        subrutine = f"{window.current_subrutine}.json"
        machine = window.current_machine
        if machine in {"B12", "A16", "K16", "E16"}:
            subrutine = f"({machine}) {subrutine}"
        with open(subrutine) as file:
            load_subrutine(window, file)
    except FileNotFoundError:
        dialog = new_subrutine_question(window)
        if dialog == QMessageBox.Yes:
            create_subrutine(window)


def load_subrutine(window: QMainWindow, file: str):
    """Carga una subrutina existente

    Args:
        window (QMainWindow): Ventana principal
        file (str): Nombre de la subrutina
    """

    create_new_tape(window)
    window.config_list = json.load(file)
    description = window.config_list[0][1]["Dsc"]
    window.config_list[0] = prefab_sub_header(window, description)
    window.save_required = False
    update_after_subrutine(window)


def create_subrutine(window: QMainWindow):
    """Crea una subrutina nueva

    Args:
        window (QMainWindow): Ventana principal
    """

    create_new_tape(window)
    description = ""
    window.config_list = [prefab_sub_header(window, description)]
    window.config_list.append(prefab_comment(window.subrutine_comment, "$1"))
    window.save_required = True
    update_after_subrutine(window)


def update_after_subrutine(window: QMainWindow):
    """Actualiza las ventanas después de la carga de subrutina

    Args:
        window (QMainWindow): Ventana principal
    """

    update_data(window)
    load_main_title(window)
    window.current_folder = window.subrutine_folder
    os.chdir(window.current_folder)


def return_to(window: QMainWindow):
    """Regresa al programa raiz de la subrutina

    Args:
        window (QMainWindow): Ventana principal
    """

    subrutine = window.config_list[0][1]["Pgr"]

    with contextlib.suppress(KeyError):
        previous_program = window.config_list[0][1]["Mnp"]
        program = f"{previous_program}.json"

        try:
            previous_program = window.config_list[0][1]["Mnp"]
            program = f"{previous_program}.json"
            with open(program) as file:
                window.config_list = json.load(file)
                update_after_subrutine(window)
                find_subrutine(window, subrutine)
        except FileNotFoundError:
            file_open_error(window)


def find_subrutine(window: QMainWindow, subrutine: str):
    """Selecciona la posición de la subrutina seleccionada

    Args:
        window (QMainWindow): Ventana principal
        subrutine (str): Subrutina seleccionada
    """

    for num, line in enumerate(window.config_list):
        with contextlib.suppress(KeyError):
            while line[1]["Sub"] == subrutine:
                window.current_selection = [num]
                update_config_widget_selection(window)
                update_tape1_widget_selection(window)
                update_tape2_widget_selection(window)
                break
