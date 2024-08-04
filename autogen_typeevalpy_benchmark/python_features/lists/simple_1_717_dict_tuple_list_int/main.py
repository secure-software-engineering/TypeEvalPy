# Functions are assigned as elements of a list and then called.


def func1():
    return {'ssaws': 99, 'seksn': 72, 'altwt': 7}


def func2():
    return (30, 10, 45)


def func3():
    return [14, 81, 21]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 22


b = ["Hello"]
b[0] = func4

f = b[0]()
