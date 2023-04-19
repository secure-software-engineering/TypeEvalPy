# Three variables are assigned a value via a recursive tuple assignment.


def func1():
    return 42


def func2():
    return 42.5


def func3():
    return "Hello from func3"


def func4():
    return [1,2]


def func5():
    return (1,2)


def func6():
    return {a:"Hello"}


a, (b, c) = func1, (func2, func3)
d = a()
e = b()
f = c()

a, (b, c) = func4, (func5, func6)
g = a()
h = b()
i = c()