#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as com
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, com.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, com.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, com.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, com.div(a, b)))

