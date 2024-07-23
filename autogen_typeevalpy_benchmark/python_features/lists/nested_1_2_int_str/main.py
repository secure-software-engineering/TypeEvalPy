# Lists containing lists that contain functions.


def func1():
    return 88


def func2():
    return 'gqqlq'


ls = [[func1], func2]

a = ls[0]
b = a[0]
c = b()
