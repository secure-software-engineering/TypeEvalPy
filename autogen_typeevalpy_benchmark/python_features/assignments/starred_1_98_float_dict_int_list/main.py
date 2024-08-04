# Functions are assigned to variables via starred assignment
def func1():
    return 52.84


def func2():
    return {'uyyli': 63, 'mjliq': 85, 'bskac': 38}


def func3():
    return 34


def func4():
    return [73, 93, 88]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
