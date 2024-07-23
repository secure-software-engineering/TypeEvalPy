# Functions are assigned as elements of a list and then called.


def func1():
    return [10, 66, 35]


def func2():
    return 4


def func3():
    return {'jqfnz': 36, 'ugtrv': 56, 'jufci': 18}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 25.75


b = ["Hello"]
b[0] = func4

f = b[0]()
