from subtasks import (
    header,
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
)

tasks_list = {
    "Header": {
        "Name": header.Header,
        "Description": "Inicio de programa",
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
        "Description": "        Iniciar torneados",
    },
    "Lineal_turn": {
        "Name": lineal_turn.Lineal_turn,
        "Description": "        Torneado lineal",
    },
    "Radial_turn": {
        "Name": radial_turn.Radial_turn,
        "Description": "        Torneado radial",
    },
}


def get_task_class(description):
    main_values = list(tasks_list.values())

    names_list, descriptions_list = [], []
    for dictionary in main_values:
        names_list.append(dictionary["Name"])
        descriptions_list.append(dictionary["Description"])

    description_index = descriptions_list.index(description)

    return names_list[description_index]
