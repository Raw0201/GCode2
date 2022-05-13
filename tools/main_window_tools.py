import os
import json
import tools

from tools.message_boxes import *
from tools.default_data_tools import *
from tools.buttons_tools import *
from tools.format_tools import *
from tools.config_list_tools import *
from tools.tape_lists_tools import *
from tools.file_tools import *
from tools.directories_tools import *
from tools.constants import *
from PySide6.QtWidgets import QFileDialog


def load_main_title(window) -> None:
    """Actualiza el título de la ventana"""

    app_name = "G-Code Editor"
    machine_type = window.current_machine
    file_name = window.config_file_name
    file_extension = window.file_extension
    folder = window.current_folder
    file = f"{file_name}{file_extension}"
    tape_name = f"- {folder}/{file} - " if file_name != "" else ""
    tape_description = f"{window.tape_description}"
    save_status = "*" if window.save_required else ""

    app_machine = f"{app_name} {machine_type}"
    tape_data = f"{tape_name} {tape_description}"
    main_title = f"{app_machine}  {tape_data} {save_status}"

    window.setWindowTitle(main_title)


def new_tape(window) -> None:
    """Crear un nuevo tape"""

    dialog = new_tape_question(window)
    if dialog == QMessageBox.Yes:
        create_new_tape(window)


def create_new_tape(window):
    """Crea el nuevo tape"""

    load_default_data_lists(window)
    load_default_variables(window)
    load_default_tape_conditions(window)
    load_default_machining_data(window)
    tools.buttons_tools.load_default_buttons_status(window)
    load_main_title(window)

    window.config_widget.clearContents()
    window.tape1_widget.clearContents()
    window.tape2_widget.clearContents()
    window.config_widget.setRowCount(0)
    window.tape1_widget.setRowCount(0)
    window.tape2_widget.setRowCount(0)


def open_file(window) -> None:
    """Abrir un archivo de configuración"""

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
        os.chdir(window.current_folder)

        update_data(window)
        window.save_required = False
        load_main_title(window)

    except OSError:
        return
    except KeyError:
        file_open_error(window)
        window.create_new_tape()


def save_config(window) -> None:
    """Guardar el archivo de configuración"""

    if not window.tape1_list:
        return

    update_data(window)
    update_file_dir(window)

    file = f"{window.file_name}.json"
    with open(file, "w") as file:
        json.dump(window.config_list, file)
    save_tape(window)


def save_tape(window) -> None:
    """Guardar el archivo de configuración"""

    if not window.tape1_list:
        return

    os.chdir(ROOT_DIR)
    complete_tape = make_tape(window)

    file = f"{window.file_name}{window.file_extension}"
    with open(file, "w") as tape:
        for lines in complete_tape:
            tape.write(lines + "\n")

    window.save_required = False
    load_main_title(window)


def make_tape(window) -> list:
    """Crea las líneas del tape

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


def close_app(window) -> None:
    """Cerrar la aplicación"""
    window.close()


def closeEvent(window, event) -> None:
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
        if window.helper1:
            window.helper1.close()
        event.accept()


def delete_lines(window) -> None:
    """Borra las líneas seleccionadas"""
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


def duplicate_lines(window) -> None:
    """Duplica las líneas seleccionadas"""

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


def movement(window, direction: str) -> None:
    """Valida el movimiento de las líneas seleccionadas

    Args:
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


def move_lines(window, index_list: list, direction: str) -> None:
    """Mueve las líneas de configuración

    Args:
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


def param_mod(window, parameter: str, direction: str, amount: float) -> None:
    """Modifica un parámetro en las líneas seleccionadas

    Args:
        parameter (str): Parámetro a modificar
        direction (str): Dirección de la modificación
        amount (float): Dimensión de la modificación
    """

    par = parameter
    mod = amount if direction == "up" else amount * -1

    if par in {"Sub", "Rep"}:
        mod = int(mod)
    elif window.current_machine == "OMNITURN" and par == "Fed":
        mod *= 1000

    index_list = window.current_selection
    for index in index_list:
        with contextlib.suppress(KeyError):
            modded = window.config_list[index][1][par]
            window.config_list[index][1][par] = modded + mod

    update_data(window)


def component_view(window, component: object) -> None:
    """Muestra u oculta el componente seleccionado

    Args:
        component (QtWidget): Componente a mostrar u ocultar
    """

    state = not window.window_components[component]

    if state:
        component.show()
    else:
        component.hide()

    window.window_components[component] = state


def home_position(window) -> None:
    """Obtiene la línea inicial del programa"""
    line = 0
    go_to_position(window, line)


def end_position(window) -> None:
    """Obtiene la línea final del programa"""
    line = len(window.config_list) - 1
    go_to_position(window, line)


def go_to_position(window, line):
    """Ir a la línea indicada"""
    window.config_widget.setCurrentCell(line, 0)
    window.current_selection = [line]
    update_tape1_widget_selection(window)
    update_tape2_widget_selection(window)


def block_lines(window) -> None:
    """Bloquea o desbloquea las líneas seleccionadas"""

    index_list = window.current_selection
    for index in index_list:
        with contextlib.suppress(KeyError):
            block = window.config_list[index][1]["Blk"]
            window.config_list[index][1]["Blk"] = not block
    update_data(window)


def update_data(window) -> None:
    """Actualiza pantalla después de abrir"""

    load_default_machining_data(window)
    generate_tape_lines(window, window.config_list)
    update_config_widget(window)
    update_tape_widget(window, window.tape1_widget, window.tape1_list)
    update_tape_widget(window, window.tape2_widget, window.tape2_list)
    update_config_widget_selection(window)
    update_tape1_widget_selection(window)
    update_tape2_widget_selection(window)

    window.modified_task = False


def load_menu_actions(window) -> None:
    """Cargar acciones del menú"""

    window.actionNew.triggered.connect(lambda: new_tape(window))
    window.actionOpen.triggered.connect(lambda: open_file(window))
    window.actionSave.triggered.connect(lambda: save_config(window))
    window.actionClose.triggered.connect(lambda: close_app(window))

    window.actionDelete.triggered.connect(lambda: delete_lines(window))
    window.actionDuplicate.triggered.connect(lambda: duplicate_lines(window))
    window.actionBlock.triggered.connect(lambda: block_lines(window))
    window.actionMove_up.triggered.connect(lambda: movement(window, "up"))
    window.actionMove_down.triggered.connect(lambda: movement(window, "down"))

    # window.actionGraph.triggered.connect(lambda: graph(window))
    # window.actionVersion.triggered.connect(lambda: version(window))

    window.actionShow_functions.triggered.connect(
        lambda: component_view(window, window.dock_functions)
    )
    window.actionShow_tape1_widget.triggered.connect(
        lambda: component_view(window, window.tape1_widget)
    )
    window.actionShow_tape2_widget.triggered.connect(
        lambda: component_view(window, window.tape2_widget)
    )
    window.actionShow_config_widget.triggered.connect(
        lambda: component_view(window, window.config_widget)
    )
    window.actionSubrut_up.triggered.connect(
        lambda: param_mod(window, "Sub", "up", 1.0)
    )
    window.actionSubrut_down.triggered.connect(
        lambda: param_mod(window, "Sub", "down", 1.0)
    )
    window.actionLoop_up.triggered.connect(
        lambda: param_mod(window, "Rep", "up", 1.0)
    )
    window.actionLoop_down.triggered.connect(
        lambda: param_mod(window, "Rep", "down", 1.0)
    )
    window.actionX_up.triggered.connect(
        lambda: param_mod(window, "Xin", "up", 0.001)
    )
    window.actionX_down.triggered.connect(
        lambda: param_mod(window, "Xin", "down", 0.001)
    )
    window.actionY_up.triggered.connect(
        lambda: param_mod(window, "Yin", "up", 0.001)
    )
    window.actionY_down.triggered.connect(
        lambda: param_mod(window, "Yin", "down", 0.001)
    )
    window.actionZ_up.triggered.connect(
        lambda: param_mod(window, "Zin", "up", 0.001)
    )
    window.actionZ_down.triggered.connect(
        lambda: param_mod(window, "Zin", "down", 0.001)
    )
    window.actionFeed_up.triggered.connect(
        lambda: param_mod(window, "Fed", "up", 0.001)
    )
    window.actionFeed_down.triggered.connect(
        lambda: param_mod(window, "Fed", "down", 0.001)
    )
