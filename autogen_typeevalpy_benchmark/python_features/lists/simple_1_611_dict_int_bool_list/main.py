# Functions are assigned as elements of a list and then called.


def func1():
    return {'makxr': 31, 'plnrd': 69, 'plmvo': 14}


def func2():
    return 46


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [77, 67, 49]


b = ["Hello"]
b[0] = func4

f = b[0]()
