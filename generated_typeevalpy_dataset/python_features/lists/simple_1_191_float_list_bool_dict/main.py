# Functions are assigned as elements of a list and then called.


def func1():
    return 44.17


def func2():
    return [84, 37, 94]


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'lviak': 14, 'roqbw': 72, 'saphh': 34}


b = ["Hello"]
b[0] = func4

f = b[0]()