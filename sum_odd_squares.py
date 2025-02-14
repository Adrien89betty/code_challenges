def get_number():
    n = int(input("Number ? : "))
    return n

def sum_odd_squares(n):
    odd_sum = 0
    count = 0
    num = 0

    while True:
        if count == n:
            return odd_sum
        else:
            if num % 2 != 0:
                odd_sum += num ** 2
                count += 1
            num += 1


if __name__ == '__main__':
    print(sum_odd_squares(get_number()))
