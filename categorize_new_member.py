def open_or_senior(data):
    for idx, d in enumerate(data):
        if d[0] >= 55 and d[1] > 7:
            data[idx] = "Senior"
        else:
            data[idx] = "Open"

    return data



if __name__ == '__main__':
    print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
