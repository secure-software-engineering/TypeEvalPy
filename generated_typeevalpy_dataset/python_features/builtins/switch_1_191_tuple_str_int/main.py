#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (7, 61, 47):
            return 'bkigu'
        case 'bkigu':
            return (7, 61, 47)
        case _:
            return "default"


a = func((7, 61, 47))
b = func('bkigu')
c = func(78)
