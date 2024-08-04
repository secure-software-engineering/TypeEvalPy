# Functions are assigned as elements of a list and then called.


def func1():
    return {'nsjsg': 89, 'sbhpn': 30, 'bfptl': 44}


def func2():
    return False


def func3():
    return [97, 34, 88]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (35, 44, 70)


b = ["Hello"]
b[0] = func4

f = b[0]()
