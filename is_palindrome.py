def is_palin(string):
    if not string:
        return False
    else:
        cleaned_str = string.replace(" ", "").lower()
        rev_str = ""
        for i in range(len(cleaned_str), 0, -1):
            rev_str += cleaned_str[i - 1]
        if cleaned_str == rev_str:
            return f"'{string}' is a palindrome."
        else:
            return f"'{string}' is not a palindrome."


if __name__ == "__main__":
    user_input = input("Enter a word to know weather it's a palindrome or not: ")
    print(is_palin(user_input))
