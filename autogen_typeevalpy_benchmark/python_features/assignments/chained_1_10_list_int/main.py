# Two variables are assigned a function via chained assignment.


def func1():
    return [5, 29, 32]


def func2():
    return 78


a = b = func1

c = b()

a = b = func2

d = a()
