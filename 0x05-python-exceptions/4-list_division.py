#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    division = 0
    elm = 0

    while (elm < list_length):
        try:
            division = my_list_1[elm] / my_list_2[elm]
            new_list.append(division)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            pass
        elm += 1
    return new_list
