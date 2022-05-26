def all_empty(data: dict) -> bool:
    """Verifica si todos los valores en un diccionario están vacíos

    Args:
        data (dict): Diccionario a verificar

    Returns:
        bool: Condición de datos vacíos
    """

    items_list = list(data.items())
    filtered_list = items_list[:-1]
    empties = sum(item[1] == "" for item in filtered_list)
    if empties == len(data) - 1:
        return True


def any_empty(data: dict) -> bool:
    """Verifica si hay algún valor vacío en un diccionario

    Args:
        data (dict): Diccionario a verificar

    Returns:
        bool: Condición de datos vacíos
    """

    empties = sum(value == "" for _, value in data.items())
    if empties > 0:
        return True
