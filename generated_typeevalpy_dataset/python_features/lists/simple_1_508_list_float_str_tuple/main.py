# Functions are assigned as elements of a list and then called.


def func1():
    return [87, 75, 43]


def func2():
    return 66.46


def func3():
    return 'mulqj'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (49, 1, 69)


b = ["Hello"]
b[0] = func4

f = b[0]()
