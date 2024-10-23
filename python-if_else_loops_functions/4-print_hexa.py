#!/usr/bin/python3
print("{}".format("".join("{:d} = 0x{:x}\n".format(i, i) for i in range(99))), end="")
