# Functions are assigned as elements of a list and then called.


def func1():
    return 63.67


def func2():
    return {'itmca': 76, 'ntumv': 21, 'twcsk': 18}


def func3():
    return 76


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [15, 83, 26]


b = ["Hello"]
b[0] = func4

f = b[0]()
