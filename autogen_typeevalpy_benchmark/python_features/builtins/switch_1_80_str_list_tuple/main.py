#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'tqbuf':
            return [13, 60, 57]
        case [13, 60, 57]:
            return 'tqbuf'
        case _:
            return "default"


a = func('tqbuf')
b = func([13, 60, 57])
c = func((80, 77, 95))
