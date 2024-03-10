def linear_search(list, target):
    """
        Searches for the index of the target value and returns the index in it exists and None if it doesn't
    """
    # Sequentially look for the index in the list
    for i in range(len(list)):
        # use the subscript notation to obtain the value by comparing the value at current index to the target
        if list[i] == target:
            return i
    return None


def verify(index) -> int:
    if index is not None:
        print("The number was found at index: ", index)
    else:
        print("The number does exist in the list")


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_search(my_list, 12)
verify(result)

result = linear_search(my_list, 6)
verify(result)