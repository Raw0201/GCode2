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


    Args:
        comment (str): Comentario a agregar
        side (str): Lado del programa

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


def prefab_thread_tool_call(tool: int, xin: float, zin: float) -> list:
    """Bloque prefabricado de llamada de herramienta

    Args:
        tool (int): Número de herramienta
        xin (float): Posición inicial eje X
        zin (float): Posición inicial eje Z

    Returns:
        list: Bloque prefabricado
    """

    return [
        "    Llamar herramienta",
        {
            "Tol": tool,
            "Typ": "CUCHILLA",
            "Dia": 0,
            "Spc": "ROSCAR",
            "Sde": "$1",
            "Xin": xin,
            "Yin": 0,
            "Zin": zin,
            "Blk": False,
        },
    ]


def prefab_cutoff_tool_call(tool: int, xin: float, zin: float) -> list:
    """Bloque prefabricado de llamada de herramienta

    Args:
        tool (int): Número de herramienta
        xin (float): Posición inicial eje X
        zin (float): Posición inicial eje Z

    Returns:
        list: Bloque prefabricado
    """

    return [
        "    Llamar herramienta",
        {
            "Tol": tool,
            "Typ": "CUCHILLA",
            "Dia": 0,
            "Spc": "TRONZAR",
            "Sde": "$1",
            "Xin": xin,
            "Yin": 0,
            "Zin": zin,
            "Blk": False,
        },
    ]


def prefab_tool_close(tool: int, side: str, bar: float) -> list:
    """Bloque prefabricado de cierre de herramienta

    Args:
        tool (int): Número de herramienta
        side (str): Lado del programa
        bar (float): Diámetro de la barra utilizada

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

    Args:
        speed (int): Velocidad de giro
        rotation (str): Dirección de rotación
        side (str): Lado del programa

    Returns:
        list: Bloque prefabricado
    """

    return [
        "        Giro del husillo",
        {"Spd": speed, "Rot": rotation, "Sde": side, "Blk": False},
    ]
