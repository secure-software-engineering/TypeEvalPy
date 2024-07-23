# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [2, 27, 25]


def func2():
    return {'rubyh': 74, 'zwnao': 68, 'heyid': 61}


def func3():
    return 60.75


def func4():
    return 'zveks'


def func5():
    return (43, 24, 7)


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
