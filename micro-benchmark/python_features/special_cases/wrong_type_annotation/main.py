# Wrong type annotation by developer. The correct type hint here should be Union[int, str]


from typing import Union


def func(x: int) -> Union[float, int]:
    if x > 0:
        return x
    else:
        return "Invalid input"


a = func(5)
b = func(-5)
