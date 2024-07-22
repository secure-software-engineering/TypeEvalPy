# Functions are assigned as elements of a list and then called.


def func1():
    return (37, 51, 15)


def func2():
    return False


def func3():
    return 'tvtek'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [17, 95, 61]


b = ["Hello"]
b[0] = func4

f = b[0]()
