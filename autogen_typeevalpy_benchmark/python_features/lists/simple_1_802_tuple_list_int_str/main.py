# Functions are assigned as elements of a list and then called.


def func1():
    return (76, 62, 6)


def func2():
    return [26, 35, 30]


def func3():
    return 66


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ccxsg'


b = ["Hello"]
b[0] = func4

f = b[0]()
