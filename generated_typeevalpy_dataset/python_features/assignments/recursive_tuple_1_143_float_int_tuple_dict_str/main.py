# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 37.46


def func2():
    return 26


def func3():
    return (82, 64, 61)


def func4():
    return {'imkps': 77, 'leeks': 25, 'sdxtb': 36}


def func5():
    return 'zbvbo'


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
