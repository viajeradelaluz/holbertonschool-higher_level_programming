#!/usr/bin/python3
def safe_print_division(a, b):
    division = None
    try:
        division = a / b
        return division
    except:
        return None
    finally:
        print("Inside result: {}".format(division))
