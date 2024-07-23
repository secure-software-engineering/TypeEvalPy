# Functions are assigned as elements of a list and then called.


def func1():
    return (36, 58, 24)


def func2():
    return 13.02


def func3():
    return {'obxrc': 70, 'irqph': 47, 'tmklp': 49}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 37


b = ["Hello"]
b[0] = func4

f = b[0]()
