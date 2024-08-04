#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 60.85
        case 60.85:
            return False
        case _:
            return "default"


a = func(False)
b = func(60.85)
c = func({'tjqvt': 14, 'wessm': 68, 'wrwul': 30})
