# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return (79, 50, 100)


def func3():
    return {'nqkgp': 22, 'ohwye': 4, 'xwkke': 80}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [81, 74, 34]


b = ["Hello"]
b[0] = func4

f = b[0]()
