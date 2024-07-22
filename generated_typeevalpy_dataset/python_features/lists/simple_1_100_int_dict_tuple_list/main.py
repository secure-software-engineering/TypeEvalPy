# Functions are assigned as elements of a list and then called.


def func1():
    return 75


def func2():
    return {'utmsq': 7, 'vlxah': 17, 'xezpo': 39}


def func3():
    return (100, 57, 21)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [95, 55, 99]


b = ["Hello"]
b[0] = func4

f = b[0]()
