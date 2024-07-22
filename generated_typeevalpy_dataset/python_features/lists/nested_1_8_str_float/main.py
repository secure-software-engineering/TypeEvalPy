# Lists containing lists that contain functions.


def func1():
    return 'rittz'


def func2():
    return 33.77


ls = [[func1], func2]

a = ls[0]
b = a[0]
c = b()
