#!/usr/bin/python3
def print_reverse_alternate():
    print("{}".format("".join([chr(ord('z') - i) if i % 2 == 0 else chr(ord('Z') - i) for i in range(26)])), end="")
