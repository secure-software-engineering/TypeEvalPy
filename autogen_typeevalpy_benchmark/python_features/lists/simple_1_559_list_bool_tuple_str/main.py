# Functions are assigned as elements of a list and then called.


def func1():
    return [95, 90, 63]


def func2():
    return False


def func3():
    return (18, 50, 47)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'voxhb'


b = ["Hello"]
b[0] = func4

f = b[0]()
