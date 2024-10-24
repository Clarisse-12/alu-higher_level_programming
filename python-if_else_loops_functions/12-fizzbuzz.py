#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0:
            print("Fizz", end="")
        elif i % 5 == 0:
            print("buzz", end="")
        elif i % 15 == 0:
            print("fizzbuzz", end="")
        else:
            print("{} ".format(i), end="")
