# Functions are assigned as elements of a list and then called.


def func1():
    return {'nskit': 92, 'vuzac': 5, 'duyqb': 74}


def func2():
    return [26, 13, 53]


def func3():
    return 82


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (61, 14, 90)


b = ["Hello"]
b[0] = func4

f = b[0]()
