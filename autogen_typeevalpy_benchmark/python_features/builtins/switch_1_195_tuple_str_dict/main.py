#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (27, 72, 1):
            return 'gzyhn'
        case 'gzyhn':
            return (27, 72, 1)
        case _:
            return "default"


a = func((27, 72, 1))
b = func('gzyhn')
c = func({'eldws': 64, 'bxqqe': 23, 'gomgs': 59})
