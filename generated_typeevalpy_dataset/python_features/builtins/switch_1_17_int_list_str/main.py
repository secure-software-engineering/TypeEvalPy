#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 59:
            return [56, 7, 36]
        case [56, 7, 36]:
            return 59
        case _:
            return "default"


a = func(59)
b = func([56, 7, 36])
c = func('otajh')
