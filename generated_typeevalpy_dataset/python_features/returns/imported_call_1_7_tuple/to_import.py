# This module defines 2 functions where one function calls the other
def return_func():
    return (56, 20, 76)


def func():
    return return_func
