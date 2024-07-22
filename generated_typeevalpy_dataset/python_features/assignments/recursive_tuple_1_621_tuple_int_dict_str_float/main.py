# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (56, 17, 9)


def func2():
    return 36


def func3():
    return {'glnob': 34, 'crrug': 87, 'brdhi': 40}


def func4():
    return 'lhyjo'


def func5():
    return 29.71


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
