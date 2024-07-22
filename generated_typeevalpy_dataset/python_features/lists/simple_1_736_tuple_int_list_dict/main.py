# Functions are assigned as elements of a list and then called.


def func1():
    return (55, 36, 42)


def func2():
    return 46


def func3():
    return [2, 81, 28]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'wykdy': 10, 'ossuw': 66, 'bpuyg': 64}


b = ["Hello"]
b[0] = func4

f = b[0]()
