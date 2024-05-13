def tower_builder(n_floors):
    tower_list = []
    for i in range(1, n_floors + 1):
        spaces = ' ' * (n_floors - i)
        floor = spaces + '*' * (2 * i - 1) + spaces
        tower_list.append(floor)
    return tower_list


print(tower_builder(3))
