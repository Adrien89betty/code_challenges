import re

def is_valid_IP(strng):
    
    if not strng or " " in strng:
        return False

    ip_pattern = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"

    match = re.match(ip_pattern, strng)
    if not match:
        return False

    for group in match.groups():
        if not group.isdigit():
            return False
        num = int(group)
        if num < 0 or num > 255:
            return False
        if len(group) > 1 and group[0] == '0':
            return False

    return True



# Must be positives intergers between 0 to 255.
# Must be 4 values.
# No spaces between values.
