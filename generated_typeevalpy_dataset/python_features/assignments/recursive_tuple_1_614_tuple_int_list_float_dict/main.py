# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (39, 96, 23)


def func2():
    return 72


def func3():
    return [80, 72, 94]


def func4():
    return 47.75


def func5():
    return {'omjvq': 83, 'fydnz': 22, 'vqnnl': 31}


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
