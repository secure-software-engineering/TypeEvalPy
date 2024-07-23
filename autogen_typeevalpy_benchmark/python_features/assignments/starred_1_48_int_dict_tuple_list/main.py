# Functions are assigned to variables via starred assignment
def func1():
    return 100


def func2():
    return {'dqaiw': 58, 'wxtob': 59, 'vdfea': 78}


def func3():
    return (38, 59, 9)


def func4():
    return [10, 47, 94]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
