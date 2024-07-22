# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'gumoe': 43, 'xffxu': 28, 'hmyhl': 57}


def func2():
    return 'zdqyo'


x = lambda x: x()

a = x(func1)

b = x(func2)
