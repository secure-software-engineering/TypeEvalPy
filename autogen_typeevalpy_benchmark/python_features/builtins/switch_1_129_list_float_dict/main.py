#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [93, 100, 95]:
            return 47.27
        case 47.27:
            return [93, 100, 95]
        case _:
            return "default"


a = func([93, 100, 95])
b = func(47.27)
c = func({'nnrpu': 92, 'kenrk': 13, 'itwey': 76})
