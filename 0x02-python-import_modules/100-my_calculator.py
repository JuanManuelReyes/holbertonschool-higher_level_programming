#!/usr/bin/python3
if __name__ == "__main__":
        from calculator_1 import add, mul, sub, div
        import sys
        if len(sys.argv) != 4:
                print("Usage: ./100-my_calculator.py <a> <operator> <b>")
                exit(1)
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operand = sys.argv[2]
        if op == "+":
                print(f"{a} + {b} = {add(a,b)}")
        elif op == '*':
                print(f"{a} * {b} = {mul(a, b)}")
        elif op == "-":
                print(f"{a} - {b} = {sub(a,b)}")
        elif op == "/":
                print(f"{a} / {b} = {div(a,b)}")
        else:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
        exit(0)
