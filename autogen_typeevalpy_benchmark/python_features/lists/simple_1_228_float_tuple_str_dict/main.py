# Functions are assigned as elements of a list and then called.


def func1():
    return 40.21


def func2():
    return (74, 13, 81)


def func3():
    return 'behll'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'kfbfb': 33, 'kbogk': 35, 'bqsyt': 36}


b = ["Hello"]
b[0] = func4

f = b[0]()
