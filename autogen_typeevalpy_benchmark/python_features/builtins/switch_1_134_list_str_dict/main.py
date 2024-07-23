#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [14, 38, 1]:
            return 'kisfk'
        case 'kisfk':
            return [14, 38, 1]
        case _:
            return "default"


a = func([14, 38, 1])
b = func('kisfk')
c = func({'seops': 77, 'apqbq': 25, 'ylpaa': 62})
