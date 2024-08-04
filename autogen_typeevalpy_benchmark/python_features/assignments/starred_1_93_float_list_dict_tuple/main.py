# Functions are assigned to variables via starred assignment
def func1():
    return 67.78


def func2():
    return [69, 78, 30]


def func3():
    return {'ygmcy': 23, 'nlptn': 50, 'ujhhs': 80}


def func4():
    return (18, 71, 43)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
