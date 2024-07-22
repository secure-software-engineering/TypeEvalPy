# Functions are assigned as elements of a list and then called.


def func1():
    return {'lvlbn': 94, 'pkuhd': 55, 'ghmdr': 29}


def func2():
    return (74, 70, 70)


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 4.04


b = ["Hello"]
b[0] = func4

f = b[0]()
