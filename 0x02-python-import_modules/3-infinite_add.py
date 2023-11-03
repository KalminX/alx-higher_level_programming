#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    args = len(argv) - 1
    total = 0
    if args == 0:
        print(0)
    elif args == 1:
        print(argv[1])
    elif args > 1:
        for i in range(1, args + 1):
            total += int(argv[i])
        print(total)
