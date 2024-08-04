# Functions are assigned as elements of a list and then called.


def func1():
    return [81, 20, 10]


def func2():
    return 'zqbth'


def func3():
    return 86.14


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (72, 93, 73)


b = ["Hello"]
b[0] = func4

f = b[0]()
