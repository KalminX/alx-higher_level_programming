#!/usr/bin/python3
for i in range(1, 90):
    if i != 89:
        if i < 10:
            print("{:0>2}".format(i), end=", ")
        elif str(i) == str(i)[::-1]:
            continue
        elif 10 < i < 90:
            if int(str(i)[::-1]) > i:
                print("{}".format(i), end=", ")
    else:
        print("{}".format(i))
