# Functions are assigned as elements of a list and then called.


def func1():
    return 73.22


def func2():
    return (18, 75, 10)


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [97, 95, 6]


b = ["Hello"]
b[0] = func4

f = b[0]()
