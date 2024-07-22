# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (12, 65, 77)


def func2():
    return 'ualwq'


def func3():
    return {'nluyr': 19, 'hltld': 13, 'peqbg': 85}


def func4():
    return [21, 80, 97]


def func5():
    return 17.87


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
