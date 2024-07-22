#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 42.67
        case 42.67:
            return False
        case _:
            return "default"


a = func(False)
b = func(42.67)
c = func({'yrlfj': 17, 'nuwox': 90, 'cvewy': 38})
