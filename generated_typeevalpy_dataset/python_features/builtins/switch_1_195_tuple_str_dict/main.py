#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (66, 37, 61):
            return 'rlkkm'
        case 'rlkkm':
            return (66, 37, 61)
        case _:
            return "default"


a = func((66, 37, 61))
b = func('rlkkm')
c = func({'tcgmn': 48, 'gqjkt': 52, 'jebnr': 10})
