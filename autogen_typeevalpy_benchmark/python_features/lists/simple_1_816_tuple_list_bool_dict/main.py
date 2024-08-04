# Functions are assigned as elements of a list and then called.


def func1():
    return (6, 31, 12)


def func2():
    return [56, 78, 83]


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'llpgj': 91, 'lbitt': 78, 'phzzg': 9}


b = ["Hello"]
b[0] = func4

f = b[0]()
