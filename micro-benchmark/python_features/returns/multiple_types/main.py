# Returning multiple types from a function using type hinting.


from typing import Union


def func(x: int) -> Union[int, str]:
    if x > 0:
        return x
    else:
        return "Invalid input"


a = func(5)
b = func(-5)
