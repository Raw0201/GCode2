import tools


def generate_tape_lines(window, data_list: list):
    """Genera las líneas de tape a partir de la lista de configuración

    Args:
        data_list (list): Lista de configuración
    """

    window.tape1_list = []
    window.tape2_list = []
    window.current_config_line = 0

    for line in data_list:
        task = line[0]
        data = line[1]
        if task != "Inicio de programa":
            window.current_config_line += 1

        task_class = tools.subtasks_tools.get_task_class(task)
        task_class.processor(window, window, data)
        task_class.switcher(window, window, data)

        parameters = get_parameters(window)
        machine = window.current_machine
        tape_lines = task_class.generator(window, machine, data)

        store_tape_data(window, tape_lines, parameters)


def store_tape_data(window, tape_lines: list, parameters: dict) -> None:
    """Guarda las líneas de tape en las listas respectivas

    Args:
        tape_lines (list): Líneas generadas de tape
        parameters (dict): Diccionario de parámetros actuales
    """

    config_line = parameters["Config_line"]
    current_tool = parameters["Current_tool"]
    current_comment = parameters["Current_comment"]

    for tape_line in tape_lines[0]:
        if tape_line != "":
            window.tape1_list.append(
                (config_line, tape_line, current_tool, current_comment)
            )
    for tape_line in tape_lines[1]:
        if tape_line != "":
            window.tape2_list.append(
                (config_line, tape_line, current_tool, current_comment)
            )


def get_parameters(window) -> dict:
    """Obtiene los parámetros actuales de configuración

    Returns:
        dict: Diccionario de parámetros
    """

    return {
        "Config_line": window.current_config_line,
        "Current_tool": window.current_tool,
        "Current_comment": window.current_comment,
    }