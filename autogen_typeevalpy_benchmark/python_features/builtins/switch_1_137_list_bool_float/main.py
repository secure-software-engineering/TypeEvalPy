#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [36, 22, 63]:
            return False
        case False:
            return [36, 22, 63]
        case _:
            return "default"


a = func([36, 22, 63])
b = func(False)
c = func(88.36)
