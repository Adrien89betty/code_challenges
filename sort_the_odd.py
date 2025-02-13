def sort_array(source_array):
    new_list = []
    for d in source_array:
        if d % 2 != 0:
            new_list.append(d)

    new_list.sort()

    for idx, d in enumerate(source_array):
        if d % 2 == 0:
            new_list.insert(idx, d)

    return new_list




if __name__ == '__main__':
    print(sort_array([5, 8, 6, 3, 4]))
