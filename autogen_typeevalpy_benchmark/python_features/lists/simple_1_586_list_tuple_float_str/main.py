# Functions are assigned as elements of a list and then called.


def func1():
    return [78, 31, 81]


def func2():
    return (17, 40, 41)


def func3():
    return 27.61


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'gzdrs'


b = ["Hello"]
b[0] = func4

f = b[0]()
