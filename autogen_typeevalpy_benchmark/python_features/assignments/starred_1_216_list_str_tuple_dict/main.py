# Functions are assigned to variables via starred assignment
def func1():
    return [38, 64, 2]


def func2():
    return 'kzeka'


def func3():
    return (81, 96, 74)


def func4():
    return {'bmzqh': 52, 'xmjel': 29, 'jnves': 32}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
