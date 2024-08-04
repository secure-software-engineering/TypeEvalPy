# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return [50, 89, 18]


def func3():
    return {'yiwjy': 38, 'ezioo': 7, 'ksjpj': 44}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (6, 8, 36)


b = ["Hello"]
b[0] = func4

f = b[0]()
