#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [36, 36, 49]:
            return 70.8
        case 70.8:
            return [36, 36, 49]
        case _:
            return "default"


a = func([36, 36, 49])
b = func(70.8)
c = func('mcnky')
