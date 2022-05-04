"""
#!/usr/bin/python3

def equivalents(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return 0 


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return Nonei
    if roman_string == "":
        return 0
    res = 0
    i = 0
    while (i < len(roman_string)):
        s1 = equivalents(roman_string[i])
        if s1 == 0:
            return 0
        if (i + 1 < len(roman_string)):
            s2 = equivalents(roman_string[i + 1])
            if (s1 >= s2):
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1

    return res
"""

#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0
    num = 0
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in dic.keys():
            return 0
        elif dic[i] >= dic[j]:
            num += dic[i]
        else:
            num -= dic[i]
    num += dic[roman_string[-1]]
    return num
