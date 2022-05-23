from tools.config_tools import *


def load_main_buttons(window: QMainWindow):
    """Carga la lista de botones de la pantalla principal

    Args:
        window (QMainWindow): Ventana principal
    """

    window.program_buttons_list = (
        window.btn_header,
        window.btn_free,
        window.btn_comment,
        window.btn_subrutine,
        window.btn_collect,
        window.btn_end,
    )

    window.tool_buttons_list = (
        window.btn_tool_call,
        window.btn_tool_close,
    )

    window.machine_buttons_list = (
        window.btn_spindle,
        window.btn_spindle_index,
        window.btn_misc,
    )

    window.turning_buttons_list = (
        window.btn_turn_ini,
        window.btn_lineal_turn,
        window.btn_radial_turn,
        window.btn_thread,
        window.btn_cutoff,
    )

    window.milling_buttons_list = (
        window.btn_mill_ini,
        window.btn_mill_end,
        window.btn_lineal_mill,
        window.btn_radial_mill,
    )

    window.milling_cycle_buttons_list = (
        window.btn_flat_mill,
        window.btn_face_mill,
        window.btn_bevel_mill,
        window.btn_facing_mill,
        window.btn_slotting_mill,
        window.btn_concaver_mill,
    )

    window.drilling_buttons_list = (
        window.btn_drill_ini,
        window.btn_drill_end,
        window.btn_center,
        window.btn_drill,
        window.btn_csink,
        window.btn_ream,
    )

    window.plate_buttons_list = (
        window.btn_platter_data,
        window.btn_call_square,
        window.btn_call_flatten,
        window.btn_flatten_sub,
        window.btn_call_lineal_x,
        window.btn_lineal_rgh_x_sub,
        window.btn_call_lineal_y,
        window.btn_lineal_rgh_y_sub,
    )


def load_default_buttons_status(window: QMainWindow):
    """Actualiza estado inicial de los botones

    Args:
        window (QMainWindow): Ventana principal
    """

    for button_list in (
        window.program_buttons_list,
        window.tool_buttons_list,
        window.machine_buttons_list,
        window.turning_buttons_list,
        window.milling_buttons_list,
        window.milling_cycle_buttons_list,
        window.drilling_buttons_list,
        window.plate_buttons_list,
    ):
        for button in button_list:
            button.setEnabled(False)

    window.btn_header.setEnabled(True)


def load_main_buttons_connections(window: QMainWindow):
    """Carga las conexiones de los botones de la pantalla principal

    Args:
        window (QMainWindow): Ventana principal
    """

    window.btn_header.clicked.connect(
        lambda: collect_data(window, "Header"),
    )
    window.btn_free.clicked.connect(
        lambda: collect_data(window, "Free"),
    )
    window.btn_comment.clicked.connect(
        lambda: collect_data(window, "Comment"),
    )
    window.btn_subrutine.clicked.connect(
        lambda: collect_data(window, "Subrutine")
    )
    window.btn_collect.clicked.connect(
        lambda: collect_data(window, "Collect"),
    )
    window.btn_end.clicked.connect(
        lambda: collect_data(window, "End"),
    )
    window.btn_tool_call.clicked.connect(
        lambda: collect_data(window, "Tool_call"),
    )
    window.btn_tool_close.clicked.connect(
        lambda: collect_data(window, "Tool_close"),
    )
    window.btn_spindle.clicked.connect(
        lambda: collect_data(window, "Spindle"),
    )
    window.btn_spindle_index.clicked.connect(
        lambda: collect_data(window, "Spindle_index"),
    )
    window.btn_misc.clicked.connect(
        lambda: collect_data(window, "Misc"),
    )
    window.btn_turn_ini.clicked.connect(
        lambda: collect_data(window, "Turn_ini"),
    )
    window.btn_lineal_turn.clicked.connect(
        lambda: collect_data(window, "Lineal_turn"),
    )
    window.btn_radial_turn.clicked.connect(
        lambda: collect_data(window, "Radial_turn"),
    )
    window.btn_thread.clicked.connect(
        lambda: collect_data(window, "Thread"),
    )
