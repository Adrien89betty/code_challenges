def find_outlier(integers):
    even = []
    odd = []
    for i in integers:
        if i % 2 != 0:
            odd.append(i)
        else:
            even.append(i)
    return even[0] if len(even) == 1 else odd[0]

if __name__ == '__main__':
    print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
