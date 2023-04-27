# This program exhibits context and field sensitivity.
# The context sensitivity comes from the fact that the same Identity() function is used in different contexts.
# It is used to assign both "secret value" and 5 to value1, which could result in different behavior depending on how value1 is used later in the program.
# The field sensitivity comes from the fact that Identity() is applied to specific object fields (value1 and value2) rather than the entire object.


class SimpleClass:
    def __init__(self):
        self.value1 = ""
        self.value2 = ""


def Identity(s):
    return s


classObject = SimpleClass()
classObject.value1 = Identity("secret value")
classObject.value2 = Identity("non secret value")
classObject.value1 = Identity(5)

a = classObject.value1
