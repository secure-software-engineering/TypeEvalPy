# This module defines 2 functions where one function calls the other
def return_func():
    return True


def func():
    return return_func
