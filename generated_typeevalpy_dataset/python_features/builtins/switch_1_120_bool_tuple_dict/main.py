#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return (34, 53, 52)
        case (34, 53, 52):
            return False
        case _:
            return "default"


a = func(False)
b = func((34, 53, 52))
c = func({'eaemv': 71, 'gzama': 23, 'ixmyi': 1})
