# Functions are assigned as elements of a list and then called.


def func1():
    return [51, 44, 16]


def func2():
    return (65, 28, 100)


def func3():
    return 47.46


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'hbewt': 48, 'reaue': 66, 'tdyfw': 16}


b = ["Hello"]
b[0] = func4

f = b[0]()
