# Functions are assigned as elements of a list and then called.


def func1():
    return [22, 33, 23]


def func2():
    return 'auulj'


def func3():
    return 3.78


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'yzdrj': 63, 'tohcd': 33, 'nnemt': 99}


b = ["Hello"]
b[0] = func4

f = b[0]()
