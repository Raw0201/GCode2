import json


def save_config_file(name: str, source: list) -> None:
    if not source:
        return

    file = f"{name}.json"
    with open(file, "w") as file:
        json.dump(source, file)


def update_file_name():
    return "nada"
