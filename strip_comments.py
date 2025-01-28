def check_values(val_1, val_2):
    return isinstance(val_1, str) and isinstance(val_2, (list, tuple))

def strip_comments(strng, markers):
    try:
        if check_values(strng, markers):
            lines = strng.split("\n")
            result = []

            for line in lines:
                for mark in markers:
                    if mark in line:
                        line = line.split(mark)[0]
                result.append(line.rstrip())

            return "\n".join(result)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ("#", "!")))
