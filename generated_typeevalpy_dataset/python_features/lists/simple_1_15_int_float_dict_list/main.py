# Functions are assigned as elements of a list and then called.


def func1():
    return 36


def func2():
    return 14.21


def func3():
    return {'rbccv': 15, 'gkffi': 40, 'ddrfz': 1}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [93, 14, 47]


b = ["Hello"]
b[0] = func4

f = b[0]()
