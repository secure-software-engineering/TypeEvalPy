# Functions are assigned as elements of a list and then called.


def func1():
    return (61, 38, 65)


def func2():
    return [43, 97, 83]


def func3():
    return {'ussds': 17, 'wwdzi': 64, 'cgfit': 83}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
