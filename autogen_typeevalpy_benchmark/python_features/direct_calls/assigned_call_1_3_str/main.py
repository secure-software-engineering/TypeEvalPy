# Assign a function to a variable and then do a direct call to its return.


def return_func():
    return 'imsxq'


def func():
    a = return_func
    return a


a = func
b = a()()
