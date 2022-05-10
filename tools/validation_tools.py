def all_empty(data: dict) -> bool:
    items_list = list(data.items())
    filtered_list = items_list[:-1]
    empties = sum(item[1] == "" for item in filtered_list)
    if empties == len(data) - 1:
        return True


def any_empty(data: dict) -> bool:
    empties = sum(value == "" for _, value in data.items())
    if empties > 0:
        return True
