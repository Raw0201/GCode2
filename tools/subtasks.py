from subtasks import (
    header,
    header_sub,
    free,
    comment,
    subrutine,
    collect,
    end,
    tool_call,
    tool_close,
    spindle,
    spindle_index,
    misc,
    turn_ini,
    lineal_turn,
    radial_turn,
    thread,
    cutoff,
    mill_ini,
    mill_end,
    lineal_mill,
    radial_mill,
    drill_ini,
    drill_end,
    center_drill,
)

tasks_list = {
    "Header": {
        "Name": header.Header,
        "Description": "Inicio de programa",
    },
    "Header_sub": {
        "Name": header_sub.Header_sub,
        "Description": "Inicio de subrutina",
    },
    "Free": {
        "Name": free.Free,
        "Description": " ",
    },
    "Comment": {
        "Name": comment.Comment,
        "Description": "        Comentario",
    },
    "Subrutine": {
        "Name": subrutine.Subrutine,
        "Description": "        -> Subrutina",
    },
    "Collect": {
        "Name": collect.Collect,
        "Description": "        Recolectar pieza",
    },
    "End": {
        "Name": end.End,
        "Description": "Fin de programa",
    },
    "Tool_call": {
        "Name": tool_call.Tool_call,
        "Description": "    Llamar herramienta",
    },
    "Tool_close": {
        "Name": tool_close.Tool_close,
        "Description": "    Cerrar herramienta",
    },
    "Spindle": {
        "Name": spindle.Spindle,
        "Description": "        Giro del husillo",
    },
    "Spindle_index": {
        "Name": spindle_index.Spindle_index,
        "Description": "        Orientar husillo",
    },
    "Misc": {
        "Name": misc.Misc,
        "Description": "        Funciones misceláneas",
    },
    "Turn_ini": {
        "Name": turn_ini.Turn_ini,
        "Description": "    * Iniciar torneados",
    },
    "Lineal_turn": {
        "Name": lineal_turn.Lineal_turn,
        "Description": "        Torneado lineal",
    },
    "Radial_turn": {
        "Name": radial_turn.Radial_turn,
        "Description": "        Torneado radial",
    },
    "Thread": {
        "Name": thread.Thread,
        "Description": "        Ciclo roscado",
    },
    "Cutoff": {
        "Name": cutoff.Cutoff,
        "Description": "        Tronzado de pieza",
    },
    "Mill_ini": {
        "Name": mill_ini.Mill_ini,
        "Description": "    * Iniciar fresados",
    },
    "Mill_end": {
        "Name": mill_end.Mill_end,
        "Description": "    * Finalizar fresados",
    },
    "Lineal_mill": {
        "Name": lineal_mill.Lineal_mill,
        "Description": "        Fresado lineal",
    },
    "Radial_mill": {
        "Name": radial_mill.Radial_mill,
        "Description": "        Fresado radial",
    },
    "Drill_ini": {
        "Name": drill_ini.Drill_ini,
        "Description": "    * Iniciar perforados",
    },
    "Drill_end": {
        "Name": drill_end.Drill_end,
        "Description": "    * Finalizar perforados",
    },
    "Center_drill": {
        "Name": center_drill.Center_drill,
        "Description": "        Agujero centro",
    },
}


def get_task_class(description: str) -> object:
    """Obtiene la clase de la subtarea

    Args:
        description (str): Descripción de la subtarea

    Returns:
        object: Clase de la subtarea
    """

    main_values = list(tasks_list.values())

    names_list, descriptions_list = [], []
    for dictionary in main_values:
        names_list.append(dictionary["Name"])
        descriptions_list.append(dictionary["Description"])

    description_index = descriptions_list.index(description)

    return names_list[description_index]
