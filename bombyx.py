#!/usr/bin/python3

from sys import argv

from error import error
import evolve


def help():
    print("USAGE")
    print("\t./106bombyx n [k | i0 i1]")
    print("DESCRIPTION")
    print("\tn\tnumber of first generation individuals")
    print("\tk\tgrowth rate from 1 to 4")
    print("\ti0\tinitial generation (included)")
    print("\ti1\tfinal generation (included)")


def main(argv):
    if len(argv) is 2:
        evolve.gen100(int(argv[0]), float(argv[1]))
    else:
        evolve.bounds(int(argv[0]), int(argv[1]),int(argv[2]))


if __name__ == "__main__":
    if len(argv) is 2 and argv[1] == "-h":
        help()
        exit(0)
    elif error(argv[1:]) is 84:
        exit(84)
    main(argv[1:])
    exit(0)
