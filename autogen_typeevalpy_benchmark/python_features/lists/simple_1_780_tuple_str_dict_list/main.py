# Functions are assigned as elements of a list and then called.


def func1():
    return (30, 70, 23)


def func2():
    return 'wqubu'


def func3():
    return {'oqwot': 77, 'kftaq': 96, 'khzkf': 79}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [66, 58, 41]


b = ["Hello"]
b[0] = func4

f = b[0]()
