# Two variables are assigned a function via chained assignment.


def func1():
    return 'zgulk'


def func2():
    return [94, 72, 85]


a = b = func1

c = b()

a = b = func2

d = a()
