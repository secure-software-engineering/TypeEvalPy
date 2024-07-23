# Functions are assigned as elements of a list and then called.


def func1():
    return {'deyct': 50, 'nsryv': 63, 'rpuhs': 5}


def func2():
    return True


def func3():
    return (91, 84, 38)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [6, 34, 69]


b = ["Hello"]
b[0] = func4

f = b[0]()
