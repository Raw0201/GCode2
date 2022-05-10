from datetime import date


def ftext(text_string: str) -> str:
    return text_string.upper()


def ftape(machine: str, tape_number: int) -> str:
    if machine != "OMNITURN":
        tape_number = str(tape_number)
        if len(tape_number) < 4:
            if machine == "MAZAK":
                while len(tape_number) != 8:
                    tape_number = f"0{tape_number}"
            else:
                while len(tape_number) != 4:
                    tape_number = f"0{tape_number}"

    return tape_number


def foper(operation: str) -> float:
    result = ""
    if operation != "":
        try:
            result = eval(operation)
            result = float(fnum4(result))
        except NameError:
            result = 0
    return result


def fdia(diameter: str) -> str:
    diameter = "{0:.3f}".format(float(diameter))

    while True:
        if diameter[0] == "-":
            if diameter[1] != "0":
                break
            diameter = f"-{diameter[2:]}"
        elif diameter[0] != "0":
            break
        else:
            diameter = diameter[1:]
    diameter = "0" if diameter == ".0" else diameter

    return diameter


def fnum3(number_string: str) -> str:
    number_string = "{0:.3f}".format(float(number_string))

    while number_string[-1] == "0" and number_string[-2] != ".":
        number_string = number_string[:-1]

    while True:
        if number_string[0] == "-":
            if number_string[1] != "0":
                break
            number_string = f"-{number_string[2:]}"
        elif number_string[0] != "0":
            break
        else:
            number_string = number_string[1:]
    number_string = "0" if number_string == ".0" else number_string

    return number_string


def fnum4(number_string: str) -> str:
    number_string = "{0:.4f}".format(float(number_string))

    while number_string[-1] == "0" and number_string[-2] != ".":
        number_string = number_string[:-1]

    while True:
        if number_string[0] == "-":
            if number_string[1] != "0":
                break
            number_string = f"-{number_string[2:]}"
        elif number_string[0] != "0":
            break
        else:
            number_string = number_string[1:]
    number_string = "0" if number_string == ".0" else number_string

    return number_string


def fversion() -> str:
    return date.today().strftime("V%m.%d.%y")


def fspace() -> str:
    return " "


def fcom(tool: int, compensations: list) -> float:
    return compensations[tool] if tool in compensations else False


def fparam(parameter_value: float) -> str:
    parameter_value = str(int(float(fnum3(parameter_value)) * 10000))
    while len(parameter_value) < 10:
        parameter_value = f"0{parameter_value}"
    return parameter_value


def ffed(feed_string: str) -> str:
    try:
        feed_string = "{0:.4f}".format(float(feed_string))

        while feed_string[-1] == "0":
            feed_string = feed_string[:-1]

        while feed_string[0] == "0":
            feed_string = feed_string[1:]
    except IndexError:
        feed_string = ".0005"

    feed_string = "0" if feed_string == "." else feed_string

    return feed_string
