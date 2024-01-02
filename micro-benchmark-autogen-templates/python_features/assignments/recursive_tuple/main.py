# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return <value1>


def func2():
    return <value2>


def func3():
    return <value3>


def func4():
    return <value4>


def func5():
    return <value5>


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
