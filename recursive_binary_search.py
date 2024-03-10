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
        
            
def verify(index):
    print("Target found: ", index)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(my_list, 12)
verify(result)

result = recursive_binary_search(my_list, 6)
verify(result)