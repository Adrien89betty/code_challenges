def expanded_form(num):
    num = str(num)
    expanded = []

    for index, digit in enumerate(num):
        expanded.append(digit + '0' * (len(num) - index - 1))

    print(' + '.join(expanded))

expanded_form(4523)
