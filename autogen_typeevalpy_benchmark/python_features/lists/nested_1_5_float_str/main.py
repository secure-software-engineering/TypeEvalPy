# Lists containing lists that contain functions.


def func1():
    return 2.72


def func2():
    return 'btrdt'


ls = [[func1], func2]

a = ls[0]
b = a[0]
c = b()
