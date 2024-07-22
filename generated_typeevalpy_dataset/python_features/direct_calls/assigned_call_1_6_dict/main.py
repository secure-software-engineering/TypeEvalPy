# Assign a function to a variable and then do a direct call to its return.


def return_func():
    return {'bkjro': 33, 'xaojx': 68, 'lagho': 96}


def func():
    a = return_func
    return a


a = func
b = a()()
