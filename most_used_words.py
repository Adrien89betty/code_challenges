import re

def top_3_words(text):
    cleaned_text = re.sub(r"[^\w\s'-]", '', text)
    print(cleaned_text)

    words = cleaned_text.split()
    occ = {}

    for word in words:
        if word not in occ:
            occ[word] = words.count(word)

    sorted_occ = sorted(occ.items(), key=lambda item: item[1], reverse=True)

    top_3_words = []
    count = 0
    for k, v in sorted_occ:
        if count < 3:
            top_3_words.append(k)
            count += 1

    print(top_3_words)


# To test if the function works.
top_3_words("a a a  b  c c  d d d d  e e e e e")
