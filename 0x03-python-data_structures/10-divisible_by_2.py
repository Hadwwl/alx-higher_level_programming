#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    divided = []
    for i in my_list:
        if (i % 2) == 0:
            divided.append(True)
        else:
            divided.append(False)
    return divided
