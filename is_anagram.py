def is_anagram(wrd1, wrd2):
    if len(wrd1) != len(wrd2):
        return f"'{wrd1}' and '{wrd2}' are not anagrams."
    else:
        lst1 = list(wrd1.lower())
        for c in wrd2.lower():
            if c in lst1:
                lst1.remove(c)
        if not lst1:
            return f"'{wrd1}' and '{wrd2}' are anagrams."
        else:
            return f"'{wrd1}' and '{wrd2}' are not anagrams."


if __name__ == "__main__":
    print("This program's purpose is to find weather two words are anagrams or not.\n")
    word1 = input("First word: ")
    word2 = input("Second word: ")
    print(is_anagram(word1, word2))
