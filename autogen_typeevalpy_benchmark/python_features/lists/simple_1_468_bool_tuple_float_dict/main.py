# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return (6, 79, 78)


def func3():
    return 26.91


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'vlfgn': 84, 'zsluk': 9, 'bnrcz': 90}


b = ["Hello"]
b[0] = func4

f = b[0]()
