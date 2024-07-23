# Functions are assigned as elements of a list and then called.


def func1():
    return 21


def func2():
    return {'fzrsp': 17, 'rwdhg': 90, 'ufrpj': 95}


def func3():
    return (81, 76, 11)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [78, 1, 78]


b = ["Hello"]
b[0] = func4

f = b[0]()
