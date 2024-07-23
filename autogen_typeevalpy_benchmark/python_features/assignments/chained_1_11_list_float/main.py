# Two variables are assigned a function via chained assignment.


def func1():
    return [39, 44, 31]


def func2():
    return 39.94


a = b = func1

c = b()

a = b = func2

d = a()
