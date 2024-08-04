# This module defines 2 functions where one function calls the other
def return_func():
    return [57, 67, 100]


def func():
    return return_func
