# This module defines 2 functions where one function calls the other
def return_func():
    return (93, 39, 16)


def func():
    return return_func
