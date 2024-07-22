# Two variables are assigned a function via chained assignment.


def func1():
    return [20, 12, 8]


def func2():
    return 65


a = b = func1

c = b()

a = b = func2

d = a()
