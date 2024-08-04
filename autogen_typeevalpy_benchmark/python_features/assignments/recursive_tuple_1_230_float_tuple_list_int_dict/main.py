# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 63.56


def func2():
    return (26, 24, 2)


def func3():
    return [19, 82, 5]


def func4():
    return 31


def func5():
    return {'eiomi': 44, 'qvplf': 44, 'qodht': 24}


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
