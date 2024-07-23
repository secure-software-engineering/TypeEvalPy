#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (68, 73, 3):
            return 34.68
        case 34.68:
            return (68, 73, 3)
        case _:
            return "default"


a = func((68, 73, 3))
b = func(34.68)
c = func({'mfdlu': 21, 'hxtuz': 25, 'yhxkc': 23})
