# Two variables are assigned a function via chained assignment.


def func1():
    return 'wkdrn'


def func2():
    return 100


a = b = func1

c = b()

a = b = func2

d = a()
