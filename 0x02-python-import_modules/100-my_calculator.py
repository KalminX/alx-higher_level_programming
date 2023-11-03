#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as cal
    from sys import exit
    from sys import argv as a

    args = len(a) - 1

    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a[1] = int(a[1])
        a[3] = int(a[3])
        if a[2] == "+":
            print("{} + {} = {}".format(a[1], a[3], cal.add(a[1], a[3])))
        elif a[2] == "-":
            print("{} - {} = {}".format(a[1], a[3], cal.sub(a[1], a[3])))
        elif a[2] == "*":
            print("{} * {} = {}".format(a[1], a[3], cal.mul(a[1], a[3])))
        elif a[2] == "/":
            print("{} / {} = {}".format(a[1], a[3], cal.div(a[1], a[3])))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
