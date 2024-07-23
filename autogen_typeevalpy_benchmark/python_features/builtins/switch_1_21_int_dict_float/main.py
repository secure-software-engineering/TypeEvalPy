#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 69:
            return {'comct': 86, 'ypndk': 79, 'mkydf': 18}
        case {'comct': 86, 'ypndk': 79, 'mkydf': 18}:
            return 69
        case _:
            return "default"


a = func(69)
b = func({'comct': 86, 'ypndk': 79, 'mkydf': 18})
c = func(24.56)
