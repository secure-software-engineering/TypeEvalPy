# Functions are assigned to variables via starred assignment
def func1():
    return (97, 92, 34)


def func2():
    return 79


def func3():
    return {'ligkg': 34, 'dvjsz': 57, 'jcutc': 92}


def func4():
    return [3, 71, 98]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
