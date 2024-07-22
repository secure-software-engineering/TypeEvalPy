# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (38, 77, 88)


def func2():
    return {'ljjlh': 40, 'lkqbk': 9, 'qwpvm': 30}


def func3():
    return 75


def func4():
    return 'bepar'


def func5():
    return 16.1


def func6():
    pass


a, (b, c) = func1, (func2, func3)
i = a()
j = b()
k = c()

a, (b, (c, d)) = func1, (func2, (func3, func4))

h = d()

f, b = c, e = func5, func6

l = e()
m = f()
