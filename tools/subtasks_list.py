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
