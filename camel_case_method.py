def camel_case(s):
    words = s.split()
    new_list = []
    for word in words:
        new_list.append(word.capitalize())

    res = ''.join(new_list)
    print(res)



camel_case('this function works great')
