import json


def save_config_file(name: str, source: list) -> None:
    """Guarda la configuración en un archivo .json

    Args:
        name (str): _description_
        source (list): _description_
    """
    if not source:
        return

    file = f"{name}.json"
    with open(file, "w") as file:
        json.dump(source, file)


def update_file_name() -> str:
    """Actualiza el nombre del archivo de tape

    Returns:
        str: Nombre del archivo de tape
    """
    return "nada"
