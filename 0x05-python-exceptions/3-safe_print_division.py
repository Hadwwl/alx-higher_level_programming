#!/usr/bin/python3
def safe_print_division(a, b):
    reslt = 0
    try:
        reslt = a/ b
    except ZeroDivisionError:
        reslt = None
    finally:
        print('Inside result: ()'.format(reslt))
        return reslt
