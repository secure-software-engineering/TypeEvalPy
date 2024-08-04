# Functions are assigned as elements of a list and then called.


def func1():
    return {'kfcdw': 36, 'qemzf': 61, 'zlxcw': 1}


def func2():
    return (12, 19, 51)


def func3():
    return 88


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [3, 96, 48]


b = ["Hello"]
b[0] = func4

f = b[0]()
