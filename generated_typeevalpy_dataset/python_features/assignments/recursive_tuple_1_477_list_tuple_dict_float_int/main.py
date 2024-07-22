# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [56, 92, 89]


def func2():
    return (79, 84, 2)


def func3():
    return {'vjcdd': 62, 'ewqur': 40, 'qbpjs': 83}


def func4():
    return 91.07


def func5():
    return 72


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
