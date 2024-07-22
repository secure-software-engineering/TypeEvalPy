# Functions are assigned as elements of a list and then called.


def func1():
    return 17.47


def func2():
    return 'eyluv'


def func3():
    return (75, 87, 75)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [58, 67, 63]


b = ["Hello"]
b[0] = func4

f = b[0]()
