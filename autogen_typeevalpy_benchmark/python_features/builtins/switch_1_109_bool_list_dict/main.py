#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return [89, 5, 76]
        case [89, 5, 76]:
            return False
        case _:
            return "default"


a = func(False)
b = func([89, 5, 76])
c = func({'yuisk': 74, 'xxhkt': 72, 'jsorq': 15})
