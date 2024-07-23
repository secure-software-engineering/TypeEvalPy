# Functions are assigned as elements of a list and then called.


def func1():
    return [82, 70, 80]


def func2():
    return 46


def func3():
    return (35, 2, 73)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ivmhr'


b = ["Hello"]
b[0] = func4

f = b[0]()
