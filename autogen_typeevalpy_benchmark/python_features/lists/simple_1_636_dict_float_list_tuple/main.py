# Functions are assigned as elements of a list and then called.


def func1():
    return {'nsrsb': 2, 'chlik': 82, 'ylfls': 5}


def func2():
    return 91.22


def func3():
    return [75, 85, 61]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (30, 83, 7)


b = ["Hello"]
b[0] = func4

f = b[0]()
