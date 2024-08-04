# Functions are assigned as elements of a list and then called.


def func1():
    return {'vwuqm': 52, 'jlfur': 68, 'gjymy': 17}


def func2():
    return [79, 27, 7]


def func3():
    return 4


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (95, 63, 27)


b = ["Hello"]
b[0] = func4

f = b[0]()
