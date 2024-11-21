def is_palin(string):
    if not string:
        return False
    else:
        cleaned_str = string.replace(" ", "").lower()
        rev_str = ""
        for i in range(len(cleaned_str), 0, -1):
            rev_str += cleaned_str[i - 1]
        if cleaned_str == rev_str:
            print(f"'{string}' is a palindrome.")
        else:
            print(f"'{string}' is not a palindrome.")


is_palin("Ka ya k")
