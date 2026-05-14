def ask_check_shift():
    while True:
        value = input("Enter a value between 1 and 25: ")
        if value.isnumeric() and 1 <= int(value) <= 25:
            return int(value)
        print("Invalid value. Enter a number between 1 and 25.")

def encrypt(message, shift):
    cypher = ""
    for c in message:
        if c.isalpha():
            shifted = ord(c) + shift
            if c.islower():
                cypher += chr((shifted - ord('a')) % 26 + ord('a'))
            elif c.isupper():
                cypher += chr((shifted - ord('A')) % 26 + ord('A'))
        else:
            cypher += c
    return cypher


if __name__ == "__main__":
    user_mess = input("Enter a message to encrypt: ")
    shift_value = ask_check_shift()
    print("Encrypted message:", encrypt(user_mess, shift_value))

































"""
You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you recently.

The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
prints out the encoded text.
Test your code using the data we've provided.

Test data
Sample input:

abcxyzABCxyz 123
2

Sample output:

cdezabCDEzab 123

Sample input:

The die is cast
25

Sample output:

Sgd chd hr bzrs



 Sandbox
Code



Console
"""
