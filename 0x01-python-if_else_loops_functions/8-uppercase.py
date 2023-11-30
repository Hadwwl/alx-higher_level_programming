#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if islower(c):
            print(chr(ord(c) - 32), end='')
        else:
            print(c, end='')
    print()
