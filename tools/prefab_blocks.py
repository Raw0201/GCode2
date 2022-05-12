def prefab_space() -> list:
    """Bloque prefabricado de espacio

    Returns:
        list: Bloque prefabricado
    """

    return [
        " ",
        {
            "Fre": " ",
        },
    ]


def prefab_comment(comment: str, side: str) -> list:
    """Bloque prefabricado de comentario

    Returns:
        list: Bloque prefabricado
    """

    return [
        "        Comentario",
        {
            "Com": comment,
            "Sde": side,
            "Blk": False,
        },
    ]


def prefab_tool_close(tool: int, side: str, bar: float) -> list:
    """Bloque prefabricado de cierre de herramienta

    Returns:
        list: Bloque prefabricado
    """

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
    """Bloque prefabricado de activación de husillo

    Returns:
        list: Bloque prefabricado
    """

    return [
        "        Giro husillo",
        {"Spd": speed, "Rot": rotation, "Sde": side, "Blk": False},
    ]
