# Functions are assigned to variables via starred assignment
def func1():
    return [55, 98, 58]


def func2():
    return {'jysoj': 22, 'ykcvc': 42, 'zpqhu': 29}


def func3():
    return (51, 5, 50)


def func4():
    return 37

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
