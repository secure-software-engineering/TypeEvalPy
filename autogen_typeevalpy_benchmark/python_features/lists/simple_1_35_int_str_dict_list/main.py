# Functions are assigned as elements of a list and then called.


def func1():
    return 70


def func2():
    return 'ryyih'


def func3():
    return {'emlsu': 41, 'vyeke': 100, 'xgnog': 38}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [40, 51, 84]


b = ["Hello"]
b[0] = func4

f = b[0]()
