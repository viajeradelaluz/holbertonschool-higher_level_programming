#!/usr/bin/python3
for character in reversed(range(97, 123)):
    if character % 2 != 0:
        be_upper = 32
    else:
        be_upper = 0

    print("{:c}".format(character - be_upper), end="")
