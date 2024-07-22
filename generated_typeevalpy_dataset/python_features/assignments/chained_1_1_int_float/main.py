# Two variables are assigned a function via chained assignment.


def func1():
    return 34


def func2():
    return 78.69


a = b = func1

c = b()

a = b = func2

d = a()
