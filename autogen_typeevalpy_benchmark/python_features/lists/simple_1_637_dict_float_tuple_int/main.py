# Functions are assigned as elements of a list and then called.


def func1():
    return {'tgvyu': 16, 'rlilh': 8, 'jkazl': 4}


def func2():
    return 28.14


def func3():
    return (61, 7, 27)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 36


b = ["Hello"]
b[0] = func4

f = b[0]()
