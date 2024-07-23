# Give as a kwarg a variable previously assigned to a function.


def func2():
    return {'ozqtm': 11, 'yliny': 65, 'prbzf': 96}


def func(a):
    return a()


a = func
b = func2
c = a(a=b)
