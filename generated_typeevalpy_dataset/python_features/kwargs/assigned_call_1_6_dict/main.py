# Give as a kwarg a variable previously assigned to a function.


def func2():
    return {'rqqfp': 98, 'cbmgj': 55, 'rzimb': 52}


def func(a):
    return a()


a = func
b = func2
c = a(a=b)
