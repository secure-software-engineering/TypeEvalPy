# A lambda is passed as a parameter and that parameter is called.


def func(a):
    return a('alkbc')


y = lambda x: x + 'alkbc'

b = func(y)
