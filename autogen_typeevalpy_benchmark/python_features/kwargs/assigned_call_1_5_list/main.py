# Give as a kwarg a variable previously assigned to a function.


def func2():
    return [7, 31, 12]


def func(a):
    return a()


a = func
b = func2
c = a(a=b)
