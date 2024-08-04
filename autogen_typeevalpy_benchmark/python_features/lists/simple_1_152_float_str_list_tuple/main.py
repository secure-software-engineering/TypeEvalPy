# Functions are assigned as elements of a list and then called.


def func1():
    return 57.12


def func2():
    return 'rlacj'


def func3():
    return [15, 8, 74]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (14, 57, 80)


b = ["Hello"]
b[0] = func4

f = b[0]()
