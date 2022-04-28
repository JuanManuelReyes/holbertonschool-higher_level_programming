#!/usr/bin/python3
if __name__ == "__main__":
        import sys

        if len(sys.argv) <= 1:
            print(0);
        else:
            aux = 0
            res = 0
            for i in range(1, len(sys.argv)):
                aux = int(sys.argv[i])
                res = res + aux
            print(res)
