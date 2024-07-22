# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'svyyt': 10, 'mwfag': 79, 'jtqse': 45}


def func2():
    return (51, 65, 25)


def func3():
    return [73, 62, 82]


def func4():
    return 24.2


def func5():
    return 68


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
