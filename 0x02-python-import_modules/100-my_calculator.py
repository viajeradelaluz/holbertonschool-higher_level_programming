#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    symbols = ["+", "-", "*", "/"]
    calc = [add, sub, mul, div]

    for i, symbol in enumerate(symbols):
        if argv[2] == symbol:
            print("{:d} {:s} {:d} = {:d}".format(a, symbol, b, calc[i](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
