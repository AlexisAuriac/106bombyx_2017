#!/usr/bin/python3

import sys

from error import error
import evolve


def main(argv):
    if len(argv) is 2:
        evolve.gen100(int(argv[0]), float(argv[1]))
    else:
        evolve.bounds(int(argv[0]), int(argv[1]),int(argv[2]))


if __name__ == "__main__":
    if error(sys.argv[1:]) is 84:
        exit(84)
    main(sys.argv[1:])
    exit(0)
