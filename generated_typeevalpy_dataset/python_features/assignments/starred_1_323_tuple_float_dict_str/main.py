# Functions are assigned to variables via starred assignment
def func1():
    return (85, 39, 26)


def func2():
    return 54.34


def func3():
    return {'qinur': 97, 'cnebe': 55, 'fitnc': 67}


def func4():
    return 'awxub'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
