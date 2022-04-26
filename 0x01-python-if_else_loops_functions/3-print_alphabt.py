#!/usr/bin/python3
for char in range(97, 123):
    if char == 101 or char == 113:
        continue
    else:
        print(f"{chr(char)}", end='')
