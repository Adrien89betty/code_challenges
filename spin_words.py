def spin_words(sentence):
    words = sentence.split()
    result_list = [word[::-1] if len(word) >= 5 else word for word in words]
    return ' '.join(result_list)

if __name__ == '__main__':
    print(spin_words("Auguste est un chat"))
