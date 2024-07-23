# Functions are assigned as elements of a list and then called.


def func1():
    return {'ckelj': 65, 'quvpg': 26, 'qumaj': 80}


def func2():
    return True


def func3():
    return [9, 7, 69]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 77.87


b = ["Hello"]
b[0] = func4

f = b[0]()
