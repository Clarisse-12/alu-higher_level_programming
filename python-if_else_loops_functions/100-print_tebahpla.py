#!/usr/bin/python3
def print_reverse_alternate():
    for i in range(26):
        print("{:c}".format(122 - i - (i % 2) * 32), end="")
