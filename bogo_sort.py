import random

def is_sorted(_list):
    for index in range(len(_list) - 1):
        if _list[index] > _list[index + 1]:
            return False
    return True

def bogo_sort(items):
    """
    I'll call this a bogus sort. It randomly shuffles the list untils it's sorted
    """
    while not is_sorted(items):
        random.shuffle(items)
    return items