#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (44, 70, 29):
            return 61
        case 61:
            return (44, 70, 29)
        case _:
            return "default"


a = func((44, 70, 29))
b = func(61)
c = func({'aecnz': 90, 'fdsfd': 18, 'aciii': 34})
