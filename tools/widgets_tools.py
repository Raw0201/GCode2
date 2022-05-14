import contextlib
import tools

from PySide6.QtWidgets import QAbstractItemView, QTableWidget, QTableWidgetItem


def load_main_widgets_connections(window):
    """Carga las conexiones de los widgets de la pantalla principal"""

    window.config_widget.clicked.connect(
        lambda: widget_clicked(window, "conf")
    )
    window.tape1_widget.clicked.connect(
        lambda: widget_clicked(window, "tape1")
    )
    window.tape2_widget.clicked.connect(
        lambda: widget_clicked(window, "tape2")
    )

    window.config_widget.itemDoubleClicked.connect(
        lambda: item_modifier(window)
    )
    window.tape1_widget.itemDoubleClicked.connect(
        lambda: item_modifier(window)
    )
    window.tape2_widget.itemDoubleClicked.connect(
        lambda: item_modifier(window)
    )

    window.config_widget.itemSelectionChanged.connect(
        lambda: config_selected(window)
    )
    window.tape1_widget.itemSelectionChanged.connect(
        lambda: tape1_selected(window)
    )
    window.tape2_widget.itemSelectionChanged.connect(
        lambda: tape2_selected(window)
    )


def update_config_widget(window) -> None:
    """Actualiza los datos en el widget de configuración"""

    config_lines = window.config_list
    window.config_widget.setRowCount(len(config_lines))
    for num, line in enumerate(config_lines):
        task_name = line[0]
        window.config_widget.setItem(num, 0, QTableWidgetItem(task_name))


def update_tape_widget(window, widget: QTableWidget, tape: list):
    """Actualiza los datos en el widget de tape"""

    widget.setRowCount(len(tape))
    for num, line in enumerate(tape):
        widget.setItem(num, 0, QTableWidgetItem(line[1]))


def update_config_widget_selection(window):
    """Actualiza la selección de items en el widget de configuración"""

    all_items = [
        window.config_widget.item(index_number, 0)
        for index_number in range(len(window.config_list))
    ]

    indexes = window.current_selection
    items = [window.config_widget.item(index, 0) for index in indexes]

    items_selector(all_items, items, window.config_widget)


def update_tape1_widget_selection(window):
    """Actualiza la seleccion de items en el widget de tape1"""

    all_items = [
        window.tape1_widget.item(index_number, 0)
        for index_number in range(len(window.tape1_list))
    ]

    config_indexes = window.current_selection
    indexes = [
        num
        for num, index in enumerate(window.tape1_list)
        if index[0] in config_indexes
    ]
    items = [window.tape1_widget.item(index, 0) for index in indexes]

    items_selector(all_items, items, window.tape1_widget)


def update_tape2_widget_selection(window):
    """Actualiza la seleccion de items en el widget de tape2"""

    all_items = [
        window.tape2_widget.item(index_number, 0)
        for index_number in range(len(window.tape2_list))
    ]

    config_indexes = window.current_selection
    indexes = [
        num
        for num, index in enumerate(window.tape2_list)
        if index[0] in config_indexes
    ]
    items = [window.tape2_widget.item(index, 0) for index in indexes]

    items_selector(all_items, items, window.tape2_widget)


def items_selector(all_items: list, items: list, widget: object):
    """Selector de items en los widgets

    Args:
        all_items (list): Lista total de items en el widget
        items (list): Lista de items a seleccionar
        widget (QWidget): Widget a seleccionar
    """

    with contextlib.suppress(AttributeError, IndexError):
        for item in all_items:
            item.setSelected(False)
        for item in items:
            item.setSelected(True)
        view = QAbstractItemView
        widget.scrollToItem(items[-1], view.PositionAtCenter)


def widget_clicked(window, widget: str):
    """Recibe la señal de item seleccionado en los widgets

    Args:
        widget (str): Widget del item seleccionado
    """

    window.current_widget = widget

    if widget == "conf":
        config_selected(window)
    elif widget == "tape1":
        tape1_selected(window)
    elif widget == "tape2":
        tape2_selected(window)


def config_selected(window):
    """Actualiza la lista de índices seleccionados en la configuración"""

    if window.current_widget == "conf":
        if selected_items := window.config_widget.selectedItems():
            config_lines = []
            config_lines.extend(
                item.row() for item in selected_items if item.column() == 0
            )
            window.current_selection = sorted(list(set(config_lines)))

            update_tape1_widget_selection(window)
            update_tape2_widget_selection(window)


def tape1_selected(window):
    """Actualiza la lista de índices seleccionados en el tape1"""

    if window.current_widget == "tape1":
        if selected_items := window.tape1_widget.selectedItems():
            items_selection(window, selected_items)


def tape2_selected(window):
    """Actualiza la lista de índices seleccionados en el tape2"""

    if window.current_widget == "tape2":
        if selected_items := window.tape2_widget.selectedItems():
            items_selection(window, selected_items)


def items_selection(window, selected_items):
    """Actualiza la lista de índices seleccionados"""

    selected_list = []
    selected_list.extend(
        item.row() for item in selected_items if item.column() == 0
    )

    config_lines = [window.tape1_list[line][0] for line in selected_list]
    window.current_selection = sorted(list(set(config_lines)))

    if window.current_widget == "tape1":
        update_config_widget_selection(window)
        update_tape2_widget_selection(window)
    elif window.current_widget == "tape2":
        update_config_widget_selection(window)
        update_tape1_widget_selection(window)


def item_modifier(window) -> None:
    """Obtiene la línea de configuración a modificar"""

    line = window.current_selection
    task = window.config_list[line[0]][0]
    data = window.config_list[line[0]][1]

    task_class = tools.subtasks_tools.get_task_class(task)
    window.subtask1 = task_class(window)
    window.subtask1.modifier(data)


def update_data_widgets(window):
    """Actualiza los datos en los widgets"""

    update_config_widget(window)
    update_tape_widget(window, window.tape1_widget, window.tape1_list)
    update_tape_widget(window, window.tape2_widget, window.tape2_list)

    update_config_widget_selection(window)
    update_tape1_widget_selection(window)
    update_tape2_widget_selection(window)
