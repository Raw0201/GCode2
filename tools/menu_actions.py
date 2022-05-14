from tools.main_window_tools import *
from subtasks import version, graph

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

    window.actionGraph.triggered.connect(lambda: graph_window(window))
    window.actionVersion.triggered.connect(lambda: version_window(window))

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


def graph_window(window):
    window.subwindow = graph.Graph()
    window.subwindow.show()


def version_window(window):
    window.subwindow = version.Version()
    window.subwindow.show()
