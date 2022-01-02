#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv)

    if argc == 1:
        word = "arguments."
    elif argc == 2:
        word = "argument:"
    else:
        word = "arguments:"

    print("{:d} {:s}".format(argc - 1, word))

    for num, value in enumerate(argv):
        if num > 0:
            print("{:d}: {:s}".format(num, value))
