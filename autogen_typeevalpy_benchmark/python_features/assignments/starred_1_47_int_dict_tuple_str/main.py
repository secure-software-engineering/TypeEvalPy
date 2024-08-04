# Functions are assigned to variables via starred assignment
def func1():
    return 18


def func2():
    return {'xpurr': 46, 'vtqvi': 74, 'csxcg': 4}


def func3():
    return (36, 22, 52)


def func4():
    return 'jxvdl'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
