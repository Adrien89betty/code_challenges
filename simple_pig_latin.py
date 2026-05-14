import string

def pig_it(text):
    words = [w for w in text.split()]
    res = []
    punc = string.punctuation

    for word in words:
        if word in punc:
            res.append(word)
        else:
            first_let = word[:1]
            word = word[1:]
            res.append(word + first_let + "ay")

    return " ".join(res)



if __name__ == '__main__':
    print(pig_it("O tempora o mores !"))
