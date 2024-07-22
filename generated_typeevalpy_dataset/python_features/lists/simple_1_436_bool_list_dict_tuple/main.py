# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return [15, 93, 1]


def func3():
    return {'pgjnr': 9, 'jzdea': 9, 'rrmjh': 70}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (52, 86, 20)


b = ["Hello"]
b[0] = func4

f = b[0]()
