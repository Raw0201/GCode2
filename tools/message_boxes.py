from PySide6.QtWidgets import QMessageBox


def new_tape_question(self) -> QMessageBox:
    return QMessageBox.question(
        self,
        "Nuevo programa",
        "¿Desea comenzar un nuevo programa en blanco?",
        buttons=QMessageBox.Yes | QMessageBox.No,
        defaultButton=QMessageBox.No,
    )


def data_type_error(self) -> QMessageBox:
    return QMessageBox.critical(
        self,
        "Error en tipo de datos",
        "Tipo de datos no válido",
    )


def blank_data_error(self) -> QMessageBox:
    return QMessageBox.critical(
        self,
        "Datos requeridos faltantes",
        "No puede haber datos en blanco",
    )


def all_blank_data_error(self) -> QMessageBox:
    return QMessageBox.critical(
        self,
        "Datos requeridos faltantes",
        "No pueden quedar todos los datos en blanco",
    )


def required_data_error(self) -> QMessageBox:
    return QMessageBox.critical(
        self,
        "Datos requeridos faltantes",
        "Digite los datos requeridos para la operación",
    )


def movement_error_information(self) -> QMessageBox:
    return QMessageBox.information(
        self,
        "Movimiento no permitido",
        "El encabezado y fin de programa\nno deben ser movidos",
    )


def delete_header_information(self) -> QMessageBox:
    return QMessageBox.information(
        self,
        "Borrando encabezado",
        "El encabezado del programa no debe ser borrado",
    )


def delete_lines_warning(self) -> QMessageBox:
    return QMessageBox.warning(
        self,
        "Borrar líneas",
        "¿Desea borrar las líneas seleccionadas?",
        buttons=QMessageBox.Yes | QMessageBox.No,
        defaultButton=QMessageBox.No,
    )


def duplicate_header_information(self) -> QMessageBox:
    return QMessageBox.information(
        self,
        "Duplicando encabezado",
        "El encabezado no debe ser duplicado",
    )


def file_open_error(self) -> QMessageBox:
    return QMessageBox.critical(
        self,
        "Error al abrir archivo",
        "No se puede cargar el programa seleccionado",
    )
