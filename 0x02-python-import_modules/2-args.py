#!/usr/bin/python3
argv = input()
print("{} arguments:".format(len(argv.split())))
n = argv.split(" ")
if len(argv) > 0:
    for i in range(len(argv.split())):
        """if len(i) % 2 == 0:
            print(i)"""
        print("{}: {}".format(i+1, n[i]))
