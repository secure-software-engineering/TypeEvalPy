# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return [63, 8, 22]


def func3():
    return (15, 14, 53)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'okzve': 85, 'orsnw': 76, 'gnkjl': 85}


b = ["Hello"]
b[0] = func4

f = b[0]()
