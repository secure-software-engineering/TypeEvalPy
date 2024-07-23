# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'bwkks'


def func2():
    return {'eofvb': 14, 'vseuj': 16, 'juoav': 69}


def func3():
    return (75, 66, 2)


def func4():
    return 55


def func5():
    return 42.77


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
