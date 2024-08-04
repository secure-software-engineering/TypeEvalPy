# Functions are assigned as elements of a list and then called.


def func1():
    return [37, 17, 30]


def func2():
    return {'xuknf': 91, 'ppfvy': 19, 'qaswf': 30}


def func3():
    return (80, 15, 77)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'dhxtr'


b = ["Hello"]
b[0] = func4

f = b[0]()
