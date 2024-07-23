# Functions are assigned as elements of a list and then called.


def func1():
    return (36, 82, 95)


def func2():
    return 26


def func3():
    return {'teugj': 26, 'lwmkx': 84, 'jsfax': 54}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [94, 77, 3]


b = ["Hello"]
b[0] = func4

f = b[0]()
