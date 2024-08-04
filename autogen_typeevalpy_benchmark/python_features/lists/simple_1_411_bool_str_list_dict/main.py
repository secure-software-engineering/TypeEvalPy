# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return 'gqivh'


def func3():
    return [46, 6, 65]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ignin': 70, 'vyqsb': 78, 'ohpon': 75}


b = ["Hello"]
b[0] = func4

f = b[0]()
