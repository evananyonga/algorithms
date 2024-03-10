def recursive_binary_search(numlist, target):
    if len(numlist) == 0:
        return False
    else:
        mid_point = len(numlist)//2
        print(mid_point)
        print(numlist[mid_point])
        print(numlist[mid_point + 1:])

        if numlist[mid_point] == target:
            return True
        else:
            if numlist[mid_point] < target:
                return recursive_binary_search(numlist[mid_point+1:], target)
            else:
                return recursive_binary_search(numlist[:mid_point], target)