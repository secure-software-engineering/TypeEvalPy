# Assign a function to a variable and then do a direct call to its return.


def return_func():
    return {'bgqap': 40, 'iecgr': 100, 'ohgpz': 62}


def func():
    a = return_func
    return a


a = func
b = a()()
