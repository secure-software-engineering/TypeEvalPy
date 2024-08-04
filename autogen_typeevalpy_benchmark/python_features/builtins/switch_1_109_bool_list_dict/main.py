#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return [90, 67, 50]
        case [90, 67, 50]:
            return False
        case _:
            return "default"


a = func(False)
b = func([90, 67, 50])
c = func({'youzy': 9, 'iwbxm': 72, 'caeoo': 59})
