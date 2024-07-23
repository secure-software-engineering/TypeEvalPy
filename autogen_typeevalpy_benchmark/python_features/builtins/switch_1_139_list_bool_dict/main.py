#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [64, 58, 19]:
            return False
        case False:
            return [64, 58, 19]
        case _:
            return "default"


a = func([64, 58, 19])
b = func(False)
c = func({'dcbze': 77, 'mubxe': 54, 'vuqbz': 29})
