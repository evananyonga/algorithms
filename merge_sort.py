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

