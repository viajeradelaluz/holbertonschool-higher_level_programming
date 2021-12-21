#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if ord(character) >= 97 and ord(character) <= 122:
            be_upper = 32
        else:
            be_upper = 0

        print("{:c}".format(ord(character) - be_upper), end="")

    print()
