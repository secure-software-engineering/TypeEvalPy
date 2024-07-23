# Functions are assigned as elements of a list and then called.


def func1():
    return 'zawlk'


def func2():
    return 40


def func3():
    return (25, 46, 10)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 58.9


b = ["Hello"]
b[0] = func4

f = b[0]()
