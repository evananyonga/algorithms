def binary_search(nlist, target):
    first = 0
    last = len(nlist) - 1

    while first <= last:
        mid_point = (first + last)//2
        print(mid_point)

        if nlist[mid_point] == target:
            return mid_point
        elif nlist[mid_point] < target:
            first = mid_point + 1
        else:
            last = mid_point - 1
    return None