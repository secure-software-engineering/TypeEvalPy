# Functions are assigned as elements of a list and then called.


def func1():
    return (54, 79, 26)


def func2():
    return [55, 22, 18]


def func3():
    return {'eqmsy': 46, 'ckovv': 93, 'hrnke': 10}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 15.55


b = ["Hello"]
b[0] = func4

f = b[0]()
