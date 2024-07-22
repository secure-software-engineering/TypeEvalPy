# Functions are assigned as elements of a list and then called.


def func1():
    return 38


def func2():
    return False


def func3():
    return (79, 14, 14)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'faomd': 49, 'kdvos': 65, 'zovha': 34}


b = ["Hello"]
b[0] = func4

f = b[0]()
