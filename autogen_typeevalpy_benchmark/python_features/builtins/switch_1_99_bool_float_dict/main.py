#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 21.91
        case 21.91:
            return False
        case _:
            return "default"


a = func(False)
b = func(21.91)
c = func({'yndrw': 80, 'slclb': 15, 'olckn': 31})
