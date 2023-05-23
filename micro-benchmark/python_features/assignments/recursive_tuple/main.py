# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return "Hello from func1"


def func2():
    return 42


def func3():
    return 42.5


def func4():
    return [2, 4]


def func5():
    return {"a": "Hello"}


def func6():
    pass


a, (b, c) = func1, (func2, func3)
a()
b()
c()

a, (b, (c, d)) = func1, (func2, (func3, func4))

h = d()

f, b = c, e = func5, func6

e()
i = f()
