#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 74
        case 74:
            return False
        case _:
            return "default"


a = func(False)
b = func(74)
c = func({'ilpns': 38, 'esthg': 79, 'ayivn': 76})
