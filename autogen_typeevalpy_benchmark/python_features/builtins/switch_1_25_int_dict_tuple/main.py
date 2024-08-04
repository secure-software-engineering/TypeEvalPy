#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 61:
            return {'ooseu': 15, 'pevwq': 38, 'choxh': 15}
        case {'ooseu': 15, 'pevwq': 38, 'choxh': 15}:
            return 61
        case _:
            return "default"


a = func(61)
b = func({'ooseu': 15, 'pevwq': 38, 'choxh': 15})
c = func((37, 1, 97))
