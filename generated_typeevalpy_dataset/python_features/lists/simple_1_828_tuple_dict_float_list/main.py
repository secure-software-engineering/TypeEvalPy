# Functions are assigned as elements of a list and then called.


def func1():
    return (27, 94, 5)


def func2():
    return {'cyuvk': 67, 'bkqgk': 2, 'kkhtc': 60}


def func3():
    return 75.46


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [19, 72, 87]


b = ["Hello"]
b[0] = func4

f = b[0]()
