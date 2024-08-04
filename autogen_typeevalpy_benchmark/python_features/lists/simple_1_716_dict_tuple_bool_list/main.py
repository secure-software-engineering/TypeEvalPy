# Functions are assigned as elements of a list and then called.


def func1():
    return {'qjwgt': 63, 'fatqy': 23, 'ekkaq': 79}


def func2():
    return (65, 31, 54)


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [76, 81, 40]


b = ["Hello"]
b[0] = func4

f = b[0]()
