# Functions are assigned to variables via starred assignment
def func1():
    return (54, 92, 53)


def func2():
    return [93, 63, 12]


def func3():
    return {'nkplu': 81, 'zspqs': 8, 'uuoti': 67}


def func4():
    return 33

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
