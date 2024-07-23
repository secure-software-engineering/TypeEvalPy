# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 45.74


def func2():
    return 29


def func3():
    return [32, 25, 93]


def func4():
    return (63, 100, 20)


def func5():
    return {'xjvup': 49, 'yozfe': 68, 'osdnz': 45}


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
