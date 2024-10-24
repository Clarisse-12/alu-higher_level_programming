#!/usr/bin/python3
def print_alphabet():
    for i in range(26):
        print("{:s}".format(
            chr(122 - i) if i % 2 == 0 else chr(90 - i)),
            end=""
        )


