# Functions are assigned as elements of a list and then called.


def func1():
    return 'aeckw'


def func2():
    return (7, 39, 73)


def func3():
    return [53, 2, 48]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'rabux': 35, 'rmcly': 20, 'rylvn': 3}


b = ["Hello"]
b[0] = func4

f = b[0]()
