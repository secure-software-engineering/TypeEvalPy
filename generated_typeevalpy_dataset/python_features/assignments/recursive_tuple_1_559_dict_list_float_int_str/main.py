# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'wqugi': 72, 'jwzdr': 1, 'uuvrb': 64}


def func2():
    return [6, 6, 26]


def func3():
    return 58.79


def func4():
    return 42


def func5():
    return 'xfwhp'


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
