# Functions are assigned as elements of a list and then called.


def func1():
    return [54, 42, 25]


def func2():
    return 'eojnw'


def func3():
    return {'mwbwj': 15, 'ejvio': 72, 'fkmaz': 23}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
