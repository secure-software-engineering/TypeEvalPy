# Functions are assigned as elements of a list and then called.


def func1():
    return {'ypdpt': 93, 'flwaw': 78, 'fzopz': 24}


def func2():
    return 56.87


def func3():
    return 'ezrir'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (86, 74, 32)


b = ["Hello"]
b[0] = func4

f = b[0]()
