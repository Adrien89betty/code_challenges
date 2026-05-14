def digital_root(n):
    while n >= 10:
        digits = [int(d) for d in str(n)]
        n = sum(digits)
    return n


if __name__ == '__main__':
    print(digital_root(359))
