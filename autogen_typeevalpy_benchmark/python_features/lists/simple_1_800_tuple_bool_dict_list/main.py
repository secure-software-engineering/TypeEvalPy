# Functions are assigned as elements of a list and then called.


def func1():
    return (40, 31, 79)


def func2():
    return True


def func3():
    return {'sogcp': 45, 'glntd': 15, 'vrtmt': 81}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [81, 14, 58]


b = ["Hello"]
b[0] = func4

f = b[0]()
