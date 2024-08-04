# Functions are assigned as elements of a list and then called.


def func1():
    return (87, 59, 12)


def func2():
    return 25


def func3():
    return [48, 69, 80]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'pvkxk': 61, 'bfdvz': 85, 'uqnby': 78}


b = ["Hello"]
b[0] = func4

f = b[0]()
