# Functions are assigned as elements of a list and then called.


def func1():
    return 90


def func2():
    return {'ypuea': 96, 'zepqg': 65, 'ndrjz': 41}


def func3():
    return 'tvwem'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (33, 91, 99)


b = ["Hello"]
b[0] = func4

f = b[0]()
