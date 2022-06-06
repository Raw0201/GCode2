from tools.cnc_codes import *
from tools.formatting import *


def misc_gen(machine: str, data: list) -> list:
    """Genera las líneas de tape

    Args:
        machine (str): Tipo de máquina utilizada
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape
    """

    if machine == "B12":
        return gen_b12(data)
    elif machine == "A16":
        return gen_a16(data)
    elif machine == "K16":
        return gen_k16(data)
    elif machine == "E16":
        return gen_e16(data)
    elif machine == "OMNITURN":
        return gen_omni(data)
    elif machine == "ROMI":
        return gen_romi(data)
    elif machine == "HARDINGE":
        return gen_hardinge(data)
    elif machine == "MAZAK":
        return gen_mazak(data)


def gen_b12(data: list) -> list:
    """Genera los códigos para torno suizo B12

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    com, stp, chk, col, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[blank_space], [blank_space]]

    com = "" if com == "" else f"(- {com} -)"
    stp = swiss_m_codes[f"PARADA {stp}"] if stp != "" else ""
    chk = swiss_m_codes[f"{chk} BOQUILLA"] if chk != "" else ""
    col = swiss_m_codes[f"{col} REFRIGERANTE"] if col != "" else ""

    lines1 = [f"{blk}{stp}{chk}{col}{com}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_a16(data: list) -> list:
    """Genera los códigos para torno suizo A16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    com, stp, chk, col, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[blank_space], [blank_space]]

    com = "" if com == "" else f"(- {com} -)"
    stp = swiss_k_m_codes[f"PARADA {stp}"]
    chk = swiss_k_m_codes[f"{chk} BOQUILLA {sde}"]
    col = swiss_k_m_codes[f"{col} REFRIGERANTE"]

    lines1 = [f"{blk}{stp}{chk}{col}{com}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_k16(data: list) -> list:
    """Genera los códigos para torno suizo K16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    com, stp, chk, col, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    com = "" if com == "" else f"(- {com} -)"
    stp = swiss_k_m_codes[f"PARADA {stp}"]
    chk = swiss_k_m_codes[f"{chk} BOQUILLA {sde}"]
    col = swiss_k_m_codes[f"{col} REFRIGERANTE"]

    lines1 = [f"{blk}{stp}{chk}{col}{com}"]
    lines2 = [blank_space]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_e16(data: list) -> list:
    """Genera los códigos para torno suizo E16

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    com, stp, chk, col, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    com = "" if com == "" else f"(- {com} -)"
    stp = swiss_k_m_codes[f"PARADA {stp}"]
    chk = swiss_k_m_codes[f"{chk} BOQUILLA {sde}"]
    col = swiss_k_m_codes[f"{col} REFRIGERANTE"]

    lines1 = [f"{blk}{stp}{chk}{col}{com}"]
    lines2 = [blank_space]

    return [lines2, lines1] if sde == "$2" else [lines1, lines2]


def gen_omni(data: list) -> list:
    """Genera los códigos para torno OmniTurn

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    com, stp, chk, col, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[blank_space], [blank_space]]

    com = "" if com == "" else f"(- {com} -)"
    stp = omni_m_codes[f"PARADA {stp}"]
    chk = omni_m_codes[f"{chk} BOQUILLA"]
    col = omni_m_codes[f"{col} REFRIGERANTE"]

    lines1 = [f"{blk}{stp}{chk}{col}{com}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_romi(data: list) -> list:
    """Genera los códigos para torno Romi

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    com, stp, chk, col, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[blank_space], [blank_space]]

    com = "" if com == "" else f"(- {com} -)"
    stp = romi_m_codes[f"PARADA {stp}"]
    chk = romi_m_codes[f"{chk} BOQUILLA"]
    col = romi_m_codes[f"{col} REFRIGERANTE"]

    lines1 = [f"{blk}{stp}{chk}{col}{com}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_hardinge(data: list) -> list:
    """Genera los códigos para torno Hardinge

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    com, stp, chk, col, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[blank_space], [blank_space]]

    com = "" if com == "" else f"(- {com} -)"
    stp = hardinge_m_codes[f"PARADA {stp}"]
    chk = hardinge_m_codes[f"{chk} BOQUILLA"]
    col = hardinge_m_codes[f"{col} REFRIGERANTE"]

    lines1 = [f"{blk}{stp}{chk}{col}{com}"]
    lines2 = [blank_space]

    return [lines1, lines2]


def gen_mazak(data: list) -> list:
    """Genera los códigos para fresadora Mazak

    Args:
        data (list): Lista de datos a procesar

    Returns:
        list: Lista de líneas de tape generadas
    """

    com, stp, chk, col, sde, blk = data.values()
    blank_space = fspace()
    blk = "/" if blk else ""

    if sde == "$2":
        return [[blank_space], [blank_space]]

    com = "" if com == "" else f"(- {com} -)"
    stp = mazak_m_codes[f"PARADA {stp}"]
    chk = mazak_m_codes[f"{chk} BOQUILLA"]
    col = mazak_m_codes[f"{col} REFRIGERANTE"]

    lines1 = [f"{blk}{stp}{chk}{col}{com}"]
    lines2 = [blank_space]

    return [lines1, lines2]
