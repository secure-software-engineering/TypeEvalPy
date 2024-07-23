# Functions are assigned as elements of a list and then called.


def func1():
    return {'izlyc': 13, 'lszse': 51, 'kpprb': 75}


def func2():
    return [88, 32, 9]


def func3():
    return 7.77


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (78, 43, 92)


b = ["Hello"]
b[0] = func4

f = b[0]()
