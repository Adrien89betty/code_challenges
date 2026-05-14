import itertools

def permutations(s):
    perms = [''.join(x) for x in itertools.permutations(s)]
    sort_duplicate = sorted(list(set(perms)))
    return sort_duplicate


if __name__ == '__main__':
    print(permutations('aabb'))
