# Functions are assigned as elements of a list and then called.


def func1():
    return 65


def func2():
    return 'hxzeb'


def func3():
    return {'tzwph': 10, 'pocls': 89, 'eumyo': 93}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (74, 79, 83)


b = ["Hello"]
b[0] = func4

f = b[0]()
