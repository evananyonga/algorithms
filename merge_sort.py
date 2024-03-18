def merge_sort(_list) -> list:
    """
    Sorts a list is asending order
    Takes in a messy list
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge the sorted sublists created in the previous step
    """

    # naively sorted list is the simplest form of solution
    if len(_list) <= 1:
        return _list
    
    left_merge, right_merge = split(_list)
    left = merge_sort(left_merge)
    right = merge_sort(right_merge)

    return merge(left, right)

def split(_list):
    """
    Divide the unsorted list at midpoit into sublists
    Return two sublists
    """

    midpoint = len(_list)//2
    left = _list[:midpoint]
    right = _list[midpoint:]

    return left, right

def merge(left_list, right_list):
    """
    Merges two lists, sorting them in the process
    Returns a new merged list
    """

    l = []
    i = 0
    j = 0

    while  i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            l.append(left_list[i])
            i += 1
        else:
            l.append(right_list[j])
            j += 1

    while i < len(left_list):
        l.append(left_list[i])
        i += 1

    while j < len(right_list):
        l.append(right_list[j])
        j += 1

    return l