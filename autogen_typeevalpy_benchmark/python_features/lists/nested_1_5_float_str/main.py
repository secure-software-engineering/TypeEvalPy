# Lists containing lists that contain functions.


def func1():
    return 54.57


def func2():
    return 'rplzk'


ls = [[func1], func2]

a = ls[0]
b = a[0]
c = b()
