# Functions are assigned as elements of a list and then called.


def func1():
    return {'qdgpb': 76, 'occrp': 95, 'lqfmp': 52}


def func2():
    return (30, 59, 77)


def func3():
    return [44, 28, 21]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
