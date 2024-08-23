import sys
import math

s = input("Please enter the string you want to be alternated : ")
punc_signs = [".", "!", "?", " "]
alternated_s = []
last_letter = []
for char in s:
  if char in punc_signs or char.isdigit():
    alternated_s.append(char)
  else:
    if not last_letter or last_letter[0].islower():
      alternated_s.append(char.upper())
      last_letter = []
      last_letter.append(char.upper())
    else:
      alternated_s.append(char.lower())
      last_letter[0] = char.lower()

print(f"Here is your string AlTeRnAtEd : {"".join(alternated_s)}")
