#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dir = dir(hidden_4)
    for row in dir:
        if row[0] != '_':
            print(row)
