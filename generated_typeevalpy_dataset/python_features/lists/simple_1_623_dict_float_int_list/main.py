# Functions are assigned as elements of a list and then called.


def func1():
    return {'cdjij': 17, 'dwagr': 31, 'ifads': 28}


def func2():
    return 19.06


def func3():
    return 46


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [26, 88, 58]


b = ["Hello"]
b[0] = func4

f = b[0]()
