# Two variables are assigned a function via chained assignment.


def func1():
    return 'emfkb'


def func2():
    return 38.52


a = b = func1

c = b()

a = b = func2

d = a()
