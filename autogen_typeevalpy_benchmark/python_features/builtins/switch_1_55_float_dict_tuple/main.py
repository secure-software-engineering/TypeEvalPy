#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 42.89:
            return {'tmvbh': 99, 'vfzca': 43, 'nkzbl': 75}
        case {'tmvbh': 99, 'vfzca': 43, 'nkzbl': 75}:
            return 42.89
        case _:
            return "default"


a = func(42.89)
b = func({'tmvbh': 99, 'vfzca': 43, 'nkzbl': 75})
c = func((34, 87, 4))
