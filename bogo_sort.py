import sys
import random
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def is_sorted(_list):
    for index in range(len(_list) - 1):
        if _list[index] > _list[index + 1]:
            return False
    return True

def bogo_sort(items):
    """
    I'll call this a bogus sort. It randomly shuffles the list untils it's sorted
    """
    attempts = 0
    while not is_sorted(items):
        print(attempts)
        random.shuffle(items)
        attempts += 1
    return items

print(bogo_sort(numbers))
