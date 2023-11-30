#!/usr/bin/python3
for m in range(10):
    for n in range(1, 10):
        if m > n:
            print("(:d)(:d)".format(m, n),
                  end='\n' if m == 8 and n == 9 else ', ')
