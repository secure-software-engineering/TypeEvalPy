# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (7, 100, 50)


def func2():
    return [68, 62, 9]


def func3():
    return 87


def func4():
    return {'opcea': 28, 'tkcpf': 69, 'ionbj': 22}


def func5():
    return 8.04


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
