# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [12, 91, 12]


def func2():
    return {'sxyza': 72, 'likvx': 98, 'gqbpj': 25}


def func3():
    return 43.56


def func4():
    return (71, 26, 38)


def func5():
    return 'ojsok'


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
