# Functions are assigned as elements of a list and then called.


def func1():
    return [79, 24, 29]


def func2():
    return (31, 69, 4)


def func3():
    return {'kbeys': 92, 'xzisk': 4, 'enfwq': 52}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 77


b = ["Hello"]
b[0] = func4

f = b[0]()
