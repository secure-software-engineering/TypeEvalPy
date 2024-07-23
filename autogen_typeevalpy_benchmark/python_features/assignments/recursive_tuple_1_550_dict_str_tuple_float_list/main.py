# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ylqbh': 96, 'snhvi': 62, 'sbrxl': 97}


def func2():
    return 'bqtao'


def func3():
    return (84, 95, 20)


def func4():
    return 37.55


def func5():
    return [91, 22, 14]


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
