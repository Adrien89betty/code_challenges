def top_3_words(text):
    words = text.split()
    occ = {}

    for word in words:
        if word in occ:
            pass
        else:
            occ[word] = words.count(word)

    

    print(occ)


# To test if the function works.
top_3_words("test de test et encore test de ")
