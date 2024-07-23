# Give as a kwarg a variable previously assigned to a function.


def func2():
    return 'cdujr'


def func(a):
    return a()


a = func
b = func2
c = a(a=b)
