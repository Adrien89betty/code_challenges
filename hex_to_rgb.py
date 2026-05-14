def hex_string_to_RGB(hex_string):
    color = {
        'r': 0,
        'g': 0,
        'b': 0
    }

    hex_string = hex_string.replace('#', '')
    hex_list = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)] # slice hex code into chunks of 2.
    key_list = list(color) # Converts color keys into list of keys.
    
    for idx, i in enumerate(hex_list):
        color[key_list[idx]] = int(hex_list[idx], 16)

    return color




if __name__ == '__main__':
    print(hex_string_to_RGB("#FF9933"))


'''Convert A Hex String To RGB'''
