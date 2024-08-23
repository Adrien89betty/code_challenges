import sys
import math

string = input("Please enter a string to divide and reverse : ")
str_lentgh = len(string)

if str_lentgh % 2 == 0:
  new_str = [string[:int(str_lentgh / 2)], string[int(str_lentgh / 2):]]
  new_str.reverse()
  print("".join(new_str))
else:
  first_half = math.ceil(str_lentgh / 2)
  new_str = [string[:int(first_half)], string[int(first_half):]]
  new_str.reverse()
  print("".join(new_str))
