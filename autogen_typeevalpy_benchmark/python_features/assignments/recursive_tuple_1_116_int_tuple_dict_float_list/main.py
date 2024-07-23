# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 4


def func2():
    return (5, 19, 92)


def func3():
    return {'rtwzw': 17, 'ptnwp': 74, 'dupgu': 29}


def func4():
    return 14.73


def func5():
    return [89, 21, 4]


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
