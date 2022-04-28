#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    i = 1
    arguments = len(argv) - 1

    print(f"{arguments} {'argument' if arguments == 1 else 'arguments'}{'.' if arguments == 0 else ':'}")
    while (i <= arguments):
        print(f"{i}: {argv[i]}")
        i += 1
