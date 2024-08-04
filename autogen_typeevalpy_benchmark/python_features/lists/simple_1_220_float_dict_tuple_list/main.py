# Functions are assigned as elements of a list and then called.


def func1():
    return 8.81


def func2():
    return {'wsybl': 39, 'qiklh': 34, 'gcxlh': 89}


def func3():
    return (78, 78, 66)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [73, 6, 91]


b = ["Hello"]
b[0] = func4

f = b[0]()
