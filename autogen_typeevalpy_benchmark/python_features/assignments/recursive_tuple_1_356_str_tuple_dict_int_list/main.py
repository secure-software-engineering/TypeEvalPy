# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'krsnq'


def func2():
    return (86, 94, 40)


def func3():
    return {'kegks': 81, 'jsnfi': 50, 'ucwvh': 21}


def func4():
    return 46


def func5():
    return [97, 48, 97]


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
