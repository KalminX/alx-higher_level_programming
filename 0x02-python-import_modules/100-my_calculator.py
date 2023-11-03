#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as cal
    from sys import exit
    from sys import argv

    args = len(argv) - 1

    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        argv[1] = int(argv[1])
        argv[3] = int(argv[3])
        if argv[2] == "+":
            print("{} + {} = {}".format(argv[1], argv[3], cal.add(argv[1], argv[3])))
        elif argv[2] == "-":
            print("{} + {} = {}".format(argv[1], argv[3], cal.sub(argv[1], argv[3])))
        elif argv[2] == "*":
            print("{} + {} = {}".format(argv[1], argv[3], cal.mul(argv[1], argv[3])))
        elif argv[2] == "/":
            print("{} + {} = {}".format(argv[1], argv[3], cal.div(argv[1], argv[3])))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
