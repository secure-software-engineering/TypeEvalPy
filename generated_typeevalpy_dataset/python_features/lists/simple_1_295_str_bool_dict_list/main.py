# Functions are assigned as elements of a list and then called.


def func1():
    return 'pytgj'


def func2():
    return False


def func3():
    return {'isxeh': 76, 'rglbc': 43, 'tpwjq': 36}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [26, 16, 74]


b = ["Hello"]
b[0] = func4

f = b[0]()
