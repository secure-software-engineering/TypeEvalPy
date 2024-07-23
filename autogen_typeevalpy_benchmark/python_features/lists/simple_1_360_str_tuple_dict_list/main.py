# Functions are assigned as elements of a list and then called.


def func1():
    return 'wwlzn'


def func2():
    return (51, 8, 40)


def func3():
    return {'geakq': 19, 'exssk': 26, 'urjge': 97}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [20, 65, 69]


b = ["Hello"]
b[0] = func4

f = b[0]()
