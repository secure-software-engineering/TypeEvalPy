# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 28.39


def func2():
    return [6, 39, 50]


def func3():
    return {'yyoba': 76, 'nhgsd': 92, 'yfovs': 60}


def func4():
    return (26, 78, 83)


def func5():
    return 'vhycv'


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
