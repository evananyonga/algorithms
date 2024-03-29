def load_numbers(file_path):
    file = open(file_path, 'r')
    numlist = []
    for n in file:
        str_num = n.strip()
        numlist.append(int(str_num))
    return numlist