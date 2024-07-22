#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [86, 89, 56]:
            return (78, 14, 22)
        case (78, 14, 22):
            return [86, 89, 56]
        case _:
            return "default"


a = func([86, 89, 56])
b = func((78, 14, 22))
c = func('xglme')
