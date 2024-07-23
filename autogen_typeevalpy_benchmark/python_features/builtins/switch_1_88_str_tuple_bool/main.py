#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'svvnr':
            return (54, 89, 63)
        case (54, 89, 63):
            return 'svvnr'
        case _:
            return "default"


a = func('svvnr')
b = func((54, 89, 63))
c = func(False)
