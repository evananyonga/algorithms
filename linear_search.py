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