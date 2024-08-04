# Functions are assigned as elements of a list and then called.


def func1():
    return [32, 76, 41]


def func2():
    return 81.76


def func3():
    return (63, 23, 48)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'savig': 78, 'ynoda': 18, 'fvaax': 49}


b = ["Hello"]
b[0] = func4

f = b[0]()
