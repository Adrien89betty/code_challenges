def solution(s):
    char_list = list(s)
    new_list = []


    if len(char_list) % 2 == 0:
        for i in range(len(char_list)-1):
            if i % 2 == 0:
                new_list.append(char_list[i] + char_list[i+1])

        return new_list

    else:
        char_list.append("_")
        for i in range(len(char_list)-1):
            if i % 2 == 0:
                new_list.append(char_list[i] + char_list[i+1])

        return new_list

# solution("abcdefg")
