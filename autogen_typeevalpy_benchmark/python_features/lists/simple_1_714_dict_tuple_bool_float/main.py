# Functions are assigned as elements of a list and then called.


def func1():
    return {'pjfus': 69, 'jwizb': 31, 'htrpd': 50}


def func2():
    return (60, 1, 6)


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 25.96


b = ["Hello"]
b[0] = func4

f = b[0]()
