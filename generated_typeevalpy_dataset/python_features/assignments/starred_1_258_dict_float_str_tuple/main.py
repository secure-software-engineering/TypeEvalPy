# Functions are assigned to variables via starred assignment
def func1():
    return {'xoxgz': 84, 'ccucc': 89, 'wkhbr': 98}


def func2():
    return 66.74


def func3():
    return 'jytyg'


def func4():
    return (29, 93, 32)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
