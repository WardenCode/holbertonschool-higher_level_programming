#!/usr/bin/python3
for number in range(100):
    print("{}{}".format(int(number / 10), number % 10), end="")
    if (number != 99):
        print(", ", end="")
