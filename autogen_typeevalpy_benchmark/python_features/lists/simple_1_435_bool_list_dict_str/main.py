# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return [15, 46, 17]


def func3():
    return {'nsnwh': 63, 'takpz': 4, 'xxdgj': 52}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'jgofm'


b = ["Hello"]
b[0] = func4

f = b[0]()
