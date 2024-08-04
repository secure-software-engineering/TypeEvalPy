# Functions are assigned as elements of a list and then called.


def func1():
    return {'shezz': 38, 'lxjxj': 87, 'fqway': 25}


def func2():
    return True


def func3():
    return 41


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (75, 6, 11)


b = ["Hello"]
b[0] = func4

f = b[0]()
