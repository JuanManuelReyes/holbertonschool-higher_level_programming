#!/usr/bin/python3
for i in range(0, 26):
    char = ord('z') - i
    if i % 2 == 1:
        char = (chr(char - 97 + 65)
    else:
    char = chr(char)

    print(f"{char}", end='')
