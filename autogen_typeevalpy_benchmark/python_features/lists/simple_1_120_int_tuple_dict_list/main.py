# Functions are assigned as elements of a list and then called.


def func1():
    return 74


def func2():
    return (12, 64, 58)


def func3():
    return {'kroaq': 47, 'cmpxd': 27, 'fzidt': 11}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [48, 32, 46]


b = ["Hello"]
b[0] = func4

f = b[0]()
