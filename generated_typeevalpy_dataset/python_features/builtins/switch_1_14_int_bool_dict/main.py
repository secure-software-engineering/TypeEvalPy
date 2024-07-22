#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 32:
            return False
        case False:
            return 32
        case _:
            return "default"


a = func(32)
b = func(False)
c = func({'ziolr': 29, 'hcjod': 92, 'mzxph': 23})
