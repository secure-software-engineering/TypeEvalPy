# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return 81


def func3():
    return [99, 83, 73]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ceyad': 87, 'hzcrl': 60, 'xqrrc': 81}


b = ["Hello"]
b[0] = func4

f = b[0]()
