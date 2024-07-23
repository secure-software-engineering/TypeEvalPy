# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (20, 58, 59)


def func2():
    return 37


def func3():
    return {'iezmn': 62, 'fzrcf': 51, 'laeju': 86}


def func4():
    return [30, 92, 72]


def func5():
    return 81.07


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
