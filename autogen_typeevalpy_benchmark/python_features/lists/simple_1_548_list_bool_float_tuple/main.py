# Functions are assigned as elements of a list and then called.


def func1():
    return [8, 83, 94]


def func2():
    return True


def func3():
    return 89.96


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (33, 32, 11)


b = ["Hello"]
b[0] = func4

f = b[0]()
