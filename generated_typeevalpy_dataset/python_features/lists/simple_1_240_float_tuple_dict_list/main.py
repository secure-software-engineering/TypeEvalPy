# Functions are assigned as elements of a list and then called.


def func1():
    return 18.0


def func2():
    return (93, 41, 86)


def func3():
    return {'tvbni': 33, 'cqeem': 75, 'vptnp': 26}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [56, 98, 9]


b = ["Hello"]
b[0] = func4

f = b[0]()
