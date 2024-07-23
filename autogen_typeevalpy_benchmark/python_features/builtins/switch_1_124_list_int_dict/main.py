#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [17, 99, 14]:
            return 97
        case 97:
            return [17, 99, 14]
        case _:
            return "default"


a = func([17, 99, 14])
b = func(97)
c = func({'kcoon': 89, 'biaxk': 59, 'mqdej': 55})
