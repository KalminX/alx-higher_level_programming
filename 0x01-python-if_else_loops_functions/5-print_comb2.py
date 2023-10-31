#!/usr/bin/python3
for i in range(100):
    if i != 99:
        print(f"{i:0>2}", end=', ')
    else:
        print(i)
