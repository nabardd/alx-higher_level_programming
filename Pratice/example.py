#!/usr/bin/python3

for i in range(5):
    print("#  " * 5,)

x = y = 2

for i in range(y):
    print(" ")
for i in range(5):
    print(" " * x, end="")
    print("#" * 5)
