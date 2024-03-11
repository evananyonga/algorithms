a = [1,2,3,4,1,2,3]

def lonely_int(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        integers = arr[start]
        occurrences = arr.count(integers)
        start += 1
        if occurrences == 1:
            return integers

lonely_int(a)