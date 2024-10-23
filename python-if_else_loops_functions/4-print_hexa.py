#!/usr/bin/python3
print("{}".format("".join("{:d} = {:x}, ".format(i, i) for i in range(99))[:-2]), end="")
