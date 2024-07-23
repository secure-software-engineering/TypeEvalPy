# Functions are assigned as elements of a list and then called.


def func1():
    return [49, 8, 85]


def func2():
    return {'kltds': 79, 'xjbsb': 87, 'ynzvf': 47}


def func3():
    return (21, 62, 20)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
