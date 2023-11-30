#!/usr/bin/python3
for m in range(10):
    for n in range(m+1, 10):
        print(f"{m}{n:01d}", end=', ' if m < 8 or n < 7 else '\n')
