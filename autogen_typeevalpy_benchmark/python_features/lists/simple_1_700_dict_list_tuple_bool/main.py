# Functions are assigned as elements of a list and then called.


def func1():
    return {'lqept': 87, 'gmccl': 44, 'ndiap': 65}


def func2():
    return [42, 61, 77]


def func3():
    return (78, 38, 62)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
