def binary_search(nlist, target):
    first = 0
    last = len(nlist) - 1

    while first <= last:
        mid_point = (first + last)//2

        if nlist[mid_point] == target:
            return mid_point
        elif nlist[mid_point] < target:
            first = mid_point + 1
        else:
            last = mid_point - 1
    return None

def verify(index):
    if index is not None:
        print("The number was found at index: ", index)
    else:
        print("The number does exist in the list")


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(my_list, 12)
verify(result)

result = binary_search(my_list, 6)
verify(result)