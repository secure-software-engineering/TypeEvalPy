# Functions are assigned as elements of a list and then called.


def func1():
    return 54


def func2():
    return {'cympb': 8, 'pjwqb': 44, 'twqtw': 57}


def func3():
    return 'gtnms'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
