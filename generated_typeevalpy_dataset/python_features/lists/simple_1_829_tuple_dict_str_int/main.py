# Functions are assigned as elements of a list and then called.


def func1():
    return (98, 89, 11)


def func2():
    return {'xapya': 35, 'liddc': 53, 'nddso': 42}


def func3():
    return 'feifs'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 68


b = ["Hello"]
b[0] = func4

f = b[0]()
