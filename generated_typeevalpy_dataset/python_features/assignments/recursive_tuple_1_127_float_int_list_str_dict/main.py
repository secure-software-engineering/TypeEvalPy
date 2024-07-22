# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 13.36


def func2():
    return 99


def func3():
    return [93, 3, 26]


def func4():
    return 'qumxg'


def func5():
    return {'rdcff': 84, 'klhfw': 12, 'uswiw': 10}


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
