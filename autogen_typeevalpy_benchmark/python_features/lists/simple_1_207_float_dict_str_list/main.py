# Functions are assigned as elements of a list and then called.


def func1():
    return 49.77


def func2():
    return {'ufyme': 72, 'gszax': 24, 'wxjnf': 57}


def func3():
    return 'dwpzd'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [18, 49, 73]


b = ["Hello"]
b[0] = func4

f = b[0]()
