# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 43.69


def func2():
    return [6, 11, 62]


def func3():
    return {'yhgrh': 86, 'kqggc': 3, 'whnue': 78}


def func4():
    return 92


def func5():
    return (12, 96, 24)


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
