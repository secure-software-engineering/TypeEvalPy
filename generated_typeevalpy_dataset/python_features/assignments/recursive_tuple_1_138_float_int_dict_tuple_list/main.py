# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 75.75


def func2():
    return 54


def func3():
    return {'vcwql': 9, 'oueiq': 98, 'urvwm': 79}


def func4():
    return (39, 79, 75)


def func5():
    return [46, 61, 91]


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
