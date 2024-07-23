# Two variables are assigned a function via chained assignment.


def func1():
    return 22.95


def func2():
    return 'jhedq'


a = b = func1

c = b()

a = b = func2

d = a()
