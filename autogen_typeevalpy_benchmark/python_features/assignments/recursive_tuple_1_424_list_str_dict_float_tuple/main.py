# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [100, 29, 35]


def func2():
    return 'nnnpw'


def func3():
    return {'dgmzt': 93, 'lolqb': 32, 'hfvpt': 46}


def func4():
    return 66.46


def func5():
    return (77, 82, 21)


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
