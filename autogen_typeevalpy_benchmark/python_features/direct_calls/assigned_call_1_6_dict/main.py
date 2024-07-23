# Assign a function to a variable and then do a direct call to its return.


def return_func():
    return {'whdcv': 33, 'gloew': 89, 'gqnlc': 80}


def func():
    a = return_func
    return a


a = func
b = a()()
