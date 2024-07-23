# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'vqpcg'


def func2():
    return (38, 92, 46)


def func3():
    return {'kvoez': 99, 'kmdlm': 85, 'qcpmd': 29}


def func4():
    return [87, 91, 45]


def func5():
    return 18


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
