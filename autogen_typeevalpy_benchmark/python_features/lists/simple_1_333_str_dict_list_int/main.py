# Functions are assigned as elements of a list and then called.


def func1():
    return 'ghgtc'


def func2():
    return {'migtb': 83, 'fdreb': 31, 'blbwa': 95}


def func3():
    return [76, 57, 99]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 74


b = ["Hello"]
b[0] = func4

f = b[0]()
