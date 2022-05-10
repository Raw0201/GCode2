def prefab_space() -> list:
    return [
        " ",
        {
            "Fre": " ",
        },
    ]


def prefab_comment(comment: str, side: str) -> list:
    return [
        "        Comentario",
        {
            "Com": comment,
            "Sde": side,
            "Blk": False,
        },
    ]


def prefab_tool_close(tool: int, side: str, bar: float) -> list:
    return [
        "    Cerrar herramienta",
        {
            "Tol": tool,
            "Sde": side,
            "Dia": bar,
            "Blk": False,
        },
    ]


def prefab_spindle(speed: int, rotation: str, side: str) -> list:
    return [
        "        Giro husillo",
        {"Spd": speed, "Rot": rotation, "Sde": side, "Blk": False},
    ]
