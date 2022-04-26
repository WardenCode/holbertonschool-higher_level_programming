#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ascii_num = ord(char)
        if ascii_num >= 97 and ascii_num <= 122:
            print(f"{chr(ascii_num - 32)}", end="")
        else:
            print(f"{char}", end="")
    print("")
