# Functions are assigned as elements of a list and then called.


def func1():
    return {'srhtq': 82, 'epdnj': 92, 'yyuxf': 20}


def func2():
    return (74, 58, 35)


def func3():
    return [37, 6, 76]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 41


b = ["Hello"]
b[0] = func4

f = b[0]()
