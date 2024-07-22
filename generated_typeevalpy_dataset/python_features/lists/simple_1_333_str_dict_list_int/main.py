# Functions are assigned as elements of a list and then called.


def func1():
    return 'zevhk'


def func2():
    return {'gzuir': 89, 'kqepg': 80, 'atmjb': 43}


def func3():
    return [99, 45, 95]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 78


b = ["Hello"]
b[0] = func4

f = b[0]()
