# Functions are assigned as elements of a list and then called.


def func1():
    return (66, 31, 60)


def func2():
    return 83.57


def func3():
    return 'zkqld'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'jrxig': 35, 'fdrye': 85, 'vkyuy': 35}


b = ["Hello"]
b[0] = func4

f = b[0]()
