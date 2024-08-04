# Functions are assigned as elements of a list and then called.


def func1():
    return (61, 59, 90)


def func2():
    return [39, 53, 79]


def func3():
    return 97


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'hsesu': 47, 'mghlo': 21, 'ebern': 94}


b = ["Hello"]
b[0] = func4

f = b[0]()
