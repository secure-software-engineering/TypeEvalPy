# Functions are assigned as elements of a list and then called.


def func1():
    return {'kewtj': 21, 'gngab': 58, 'grjwl': 50}


def func2():
    return (76, 5, 52)


def func3():
    return 'kttqk'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [92, 73, 58]


b = ["Hello"]
b[0] = func4

f = b[0]()
