#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 21:
            return 45.26
        case 45.26:
            return 21
        case _:
            return "default"


a = func(21)
b = func(45.26)
c = func({'meomo': 44, 'lgxap': 38, 'ekyab': 64})
