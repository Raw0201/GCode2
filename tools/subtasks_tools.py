from subtasks import header, free, comment, subrutine, collect, end

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
        "Description": "    Comentario",
    },
    "Subrut": {
        "Name": subrutine.Subrutine,
        "Description": "    -> Subrutina",
    },
    "Collect": {
        "Name": collect.Collect,
        "Description": "    Recolectar pieza",
    },
    "End": {
        "Name": end.End,
        "Description": "Fin de programa",
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
