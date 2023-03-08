#!/usr/bin/python3
def pow(a, b):
    val = a
    for i in range(1, b):
        val = val * a
    print(val)
