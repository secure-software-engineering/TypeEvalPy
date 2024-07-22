# Functions are assigned as elements of a list and then called.


def func1():
    return 83


def func2():
    return 49.67


def func3():
    return [54, 81, 49]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'xgqpl': 3, 'abnms': 49, 'gdlsl': 95}


b = ["Hello"]
b[0] = func4

f = b[0]()
