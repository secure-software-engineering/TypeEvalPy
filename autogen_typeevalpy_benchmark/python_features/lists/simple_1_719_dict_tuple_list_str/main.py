# Functions are assigned as elements of a list and then called.


def func1():
    return {'cqxxg': 81, 'afnvo': 26, 'bvqed': 96}


def func2():
    return (100, 97, 88)


def func3():
    return [54, 45, 17]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ycclq'


b = ["Hello"]
b[0] = func4

f = b[0]()
