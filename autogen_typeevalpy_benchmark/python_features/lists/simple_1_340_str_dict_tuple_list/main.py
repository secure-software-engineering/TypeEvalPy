# Functions are assigned as elements of a list and then called.


def func1():
    return 'jxjyh'


def func2():
    return {'crsvk': 35, 'nzlbh': 52, 'rbynl': 96}


def func3():
    return (67, 93, 62)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [5, 38, 69]


b = ["Hello"]
b[0] = func4

f = b[0]()
