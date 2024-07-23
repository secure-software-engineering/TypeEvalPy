# Functions are assigned as elements of a list and then called.


def func1():
    return {'dtcjg': 88, 'stfbw': 3, 'uneai': 30}


def func2():
    return [24, 32, 97]


def func3():
    return (25, 96, 47)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 74.12


b = ["Hello"]
b[0] = func4

f = b[0]()
