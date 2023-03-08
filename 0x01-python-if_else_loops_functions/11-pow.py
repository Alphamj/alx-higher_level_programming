#!/usr/bin/python3
def pow(a, b):
    val = a
    for i in range(b):
        if b < 0:
            val = b / a
            return val
        elif b > 0:
            val = val * a
            return val
        else:
            val = 1
            return val
