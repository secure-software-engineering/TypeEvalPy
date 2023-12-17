# This module defines 2 functions where one function calls the other
def return_func():
    return "Hello from return_func"


def func():
    return return_func
