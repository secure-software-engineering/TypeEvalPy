# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (87, 84, 57)


def func2():
    return 64.97


def func3():
    return {'adkzr': 20, 'cptmw': 2, 'nvqcc': 7}


def func4():
    return [10, 72, 30]


def func5():
    return 'npjqz'


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
