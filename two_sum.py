def two_sum(numbers, target):
    complements = {}
    for index, num in enumerate(numbers):
        diff = target - num
        if diff in complements:
            return complements[diff], index
        complements[num] = index
    return None

