# Two variables are assigned a function via chained assignment.


def func1():
    return 45.41


def func2():
    return 'khgyl'


a = b = func1

c = b()

a = b = func2

d = a()
