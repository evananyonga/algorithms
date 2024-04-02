import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def selection_sort(list_of_nos):
    sorted_list = []
    print("%-25s %-25s" % (list_of_nos, sorted_list))
    for ind in range(len(list_of_nos)):
        index_to_move = index_of_min(list_of_nos)
        sorted_list.append(list_of_nos.pop(index_to_move))
        print("%-25s %-25s" % (list_of_nos, sorted_list))
    return sorted_list

def index_of_min(vals):
    smallest_index = 0
    for i in range(1, len(vals)):
        if vals[i] < vals[smallest_index]:
            smallest_index = i
    return smallest_index


print(selection_sort(numbers))

# evaluate time it takes to run program via terminal
# `time python selection_sort.py num.txt` 
# print(index_of_min(numbers))